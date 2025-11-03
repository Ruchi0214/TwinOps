# 🌐 TwinOps.AI  
### Smart Technician Assignment with AI + AWS + Blockchain Audit  

> **Tagline:** Smarter Technicians, Faster Resolutions, Trusted Operations.
Automating MSP operations with intelligent technician dispatch and verifiable blockchain audit trails.  
> Built for rapid, reliable, and transparent field operations.

---

## 🚀 Overview
TwinOps.AI is an **AI-powered operations assistant** that assigns the best-suited technician to each service task based on skill, availability, and efficiency.  
All assignments are **logged to AWS S3** and **verified on Polygon blockchain**, ensuring transparency and trust.

---

## 🧠 Core Features
| Feature | Description |
|----------|--------------|
| 🤖 **AI Agent** | Intelligent matching between task requirements and technician skills. |
| ☁️ **AWS Integration** | EC2-hosted FastAPI backend and S3 data storage for technician/task logs. |
| 🔗 **Blockchain Audit** | Every assignment emits an on-chain event on Polygon Mumbai testnet. |
| 💻 **Figma / React Frontend** | Clean dashboard to assign tasks and view blockchain TX links. |
| 📊 **Data-Driven Insights** | Technician efficiency analytics and historical logs stored on S3. |

---

## 🧩 Architecture    
<p align="center"><b>⚙️ System Architecture</b></p>
```
TwinOps Web App (Next.js + React)
        ↓
FastAPI / Node.js Backend (EC2 or Lambda)
        ↓
Amazon Bedrock Agent (Gemini + LangChain + PyTorch logic)
        ↓
 ┌──────────────┬──────────────┬──────────────┐
 | Task Agent   | Audit Agent  | Support Agent|
 | (Bedrock)    | (S3 + Chain) | (Gemini/Nova)|
 └──────────────┴──────────────┴──────────────┘
        ↓
AWS S3 (Logs & Data) + PostgreSQL/MongoDB
        ↓
Polygon Blockchain (Immutable Audit Trail)
        ↓
AWS CloudWatch (Monitoring + Observability)

```
```
---
🧠 **Flow Summary:**
1. Frontend (Next.js + React) — User submits task request.
2. Backend (FastAPI / Node.js on EC2) — Processes request, triggers AI pipeline.
3. Bedrock Agent Layer — Combines Gemini + LangChain + PyTorch for smart matching.
4. Agents:
   🧠 Task Agent → Chooses best technician.
   🧾 Audit Agent → Logs assignment to S3 + Polygon Blockchain.
   💬 Support Agent → Provides AI insights or chat summaries.
5. Data Layer (S3 + PostgreSQL/MongoDB) — Stores task data, technician efficiency logs.
6. Blockchain Layer (Polygon) — Immutable audit trail for compliance.
7. Monitoring (CloudWatch) — Tracks system performance and uptime
---
```markdown
![AWS](https://img.shields.io/badge/Cloud-AWS-orange?style=for-the-badge&logo=amazonaws)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-brightgreen?style=for-the-badge&logo=fastapi)
![Polygon](https://img.shields.io/badge/Blockchain-Polygon-purple?style=for-the-badge&logo=polygon)
![Python](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python)
![Figma](https://img.shields.io/badge/Design-Figma-pink?style=for-the-badge&logo=figma)
```
---

## 🧰 Tech Stack
**Frontend:** Figma Make / React + Tailwind CSS  
**Backend:** Python • FastAPI • LangChain • boto3  
**Blockchain:** Solidity • web3.py • Polygon Mumbai  
**Cloud:** AWS EC2 • S3 • IAM  
**Tools:** GitHub • Canva • Figma • Loom

---
## ⚙️ Setup & Run Locally

### 1️⃣ Clone Repository
https://github.com/Ruchi0214/TwinOps.git
cd TwinOps/backend

###2️⃣ Create Python Environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 🌐 TwinOps.AI Environment Configuration
# ======================================

# ---- AWS ----
AWS_REGION=us-east-1
TWINOPS_S3_BUCKET=twinops-logs-ruchi123
TWINOPS_FRONTEND_BUCKET=twinops-frontend-ruchi123

# ---- DATA ----
TECH_CSV=data/technicians.csv
TASK_CSV=data/tasks.csv

# ---- OPTIONAL AI / LLM ----
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>    
GEMINI_API_KEY=<YOUR_GEMINI_API_KEY>     

# ======================================
# ⚠️ NOTES:
# - Do NOT commit your real .env file.
# - Keep private keys & API keys local.
# - This .env.example is safe for public repos.
# ======================================


###
4️⃣ Run API
uvicorn app:app --reload --host 0.0.0.0 --port 8000

#☁️ Deploy to AWS
###🧩 EC2 (Backend)
# SSH into instance
ssh -i KEY.PEM ubuntu@18.216.213.230

# Inside EC2
git clone https://github.com/Ruchi0214/TwinOps.git
cd TwinOps/backend
source .venv/bin/activate
uvicorn app:app --host 0.0.0.0 --port 8000

#🪣 S3 (Frontend + Data)
aws s3 mb s3://twinops-frontend-name --region us-east-2
aws s3 sync frontend/build/ s3://twinops-frontend-name --acl public-read

# ---- BLOCKCHAIN ----
POLYGON_RPC=https://polygon-mumbai.infura.io/v3/3a9xYzYourInfuraKeyHere
WALLET_PRIVATE_KEY=0x<YOUR_PRIVATE_KEY_DO_NOT_PUSH>
CONTRACT_ADDRESS=0xAbCdEf1234567890abcdef1234567890abcdef12
CONTRACT_ABI_PATH=backend/abi.json
