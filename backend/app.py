# backend/app.py
import os, json, datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import boto3
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

# CONFIG (set these in .env file)
S3_BUCKET = os.getenv("TWINOPS_S3_BUCKET")  # e.g. twinops-logs-yourname
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
POLYGON_RPC = os.getenv("POLYGON_RPC")  # Infura/Alchemy Mumbai RPC
PRIVATE_KEY = os.getenv("WALLET_PRIVATE_KEY")  # wallet with test MATIC (Mumbai)
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # deployed contract address
CONTRACT_ABI_PATH = os.getenv("CONTRACT_ABI_PATH", "abi.json")

# load data
TECH_CSV = os.getenv("TECH_CSV", "data/technicians.csv")
if not os.path.exists(TECH_CSV):
    # create tiny fallback dataset
    import csv
    os.makedirs("data", exist_ok=True)
    with open(TECH_CSV, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["TechnicianID","Name","Skill","Experience(Years)","Availability","Efficiency(%)"])
        writer.writerow([1,"Alice Johnson","Network",5,"Available",92])
        writer.writerow([2,"Bob Kumar","Hardware",4,"Available",88])

tech_df = pd.read_csv(TECH_CSV)

app = FastAPI(title="TwinOps Prototype API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# S3 client
s3 = boto3.client("s3", region_name=AWS_REGION)

# Web3 setup (if configured)
w3 = None
account = None
contract = None
if POLYGON_RPC and PRIVATE_KEY and CONTRACT_ADDRESS and os.path.exists(CONTRACT_ABI_PATH):
    w3 = Web3(Web3.HTTPProvider(POLYGON_RPC))
    account = w3.eth.account.from_key(PRIVATE_KEY)
    with open(CONTRACT_ABI_PATH) as f:
        abi = json.load(f)
    contract = w3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=abi)

def assign_task_by_skill(skill: str):
    df = tech_df[tech_df["Skill"].str.contains(skill, case=False, na=False)]
    df = df[df["Availability"].str.lower() == "available"]
    if df.empty:
        df = tech_df[tech_df["Skill"].str.contains(skill, case=False, na=False)]
    if df.empty:
        return {"assigned": None, "reason": "no technician with skill"}
    picked = df.sort_values("Efficiency(%)", ascending=False).iloc[0]
    return {"assigned": picked["Name"], "skill": picked["Skill"], "eff": int(picked["Efficiency(%)"])}

def log_to_s3(taskid: str, payload: dict):
    key = f"logs/{taskid}_{int(datetime.datetime.utcnow().timestamp())}.json"
    s3.put_object(Bucket=S3_BUCKET, Key=key, Body=json.dumps(payload).encode("utf-8"))
    return key

def record_on_chain(task: str, technician: str):
    if not contract or not w3 or not account:
        return None
    tx = contract.functions.recordAssignment(task, technician).build_transaction({
        "from": account.address,
        "nonce": w3.eth.get_transaction_count(account.address),
        "gas": 300000,
        "gasPrice": w3.to_wei('2', 'gwei'),
        "chainId": 80001
    })
    signed = account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    return w3.to_hex(tx_hash)

@app.get("/assign")
def assign(task: str, skill: str):
    if not task or not skill:
        raise HTTPException(status_code=400, detail="task and skill required")
    result = assign_task_by_skill(skill)
    payload = {"task": task, "skill": skill, "result": result, "ts": datetime.datetime.utcnow().isoformat()}
    # Try S3 log (best effort)
    try:
        s3_key = log_to_s3(task.replace(" ", "_"), payload)
        payload["s3_key"] = s3_key
    except Exception as e:
        payload["s3_error"] = str(e)
    # Try blockchain
    try:
        tx = record_on_chain(task, result.get("assigned") or "None")
        payload["tx"] = tx
    except Exception as e:
        payload["chain_error"] = str(e)
    return payload

@app.get("/health")
def health():
    return {"status": "ok"}
