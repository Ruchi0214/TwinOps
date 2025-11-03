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

## 🧩 Architecture              ┌
*TwinOps Web App (Next.js + React)
        ↓
FastAPI / Node.js Backend (EC2)
        ↓
Amazon Bedrock Agent (Gemini + LangChain + PyTorch logic)
        ↓
 ┌──────────────┬──────────────┬──────────────┐
 | Task Agent   | Audit Agent  | Support Agent|
 | (Bedrock)    | (S3 + Chain) | (Gemini     )|
 └──────────────┴──────────────┴──────────────┘
        ↓
AWS S3 (Logs & Data) + PostgreSQL/MongoDB
        ↓
Polygon Blockchain (Immutable Audit Trail)
        ↓
AWS CloudWatch (Monitoring + Observability)

---
🧠 **Flow Summary:**
1. **User** interacts with the **TwinOps.AI frontend** (Figma Make or React hosted on S3).  
2. The **frontend calls FastAPI** (deployed on AWS EC2) via REST API.  
3. **FastAPI Agent** processes data and:
   - Fetches & logs tasks to **AWS S3**
   - Sends audit record to **Polygon Blockchain**
   - Returns technician + TX info to the UI  
4. **Results** are visualized instantly — with blockchain proof and stored S3 logs.

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

###3️⃣ Add Environment Variables(.env)
# ==============================================
# 🌐 TwinOps.AI - Environment Configuration
# ==============================================

# ---- AWS CONFIGURATION ----
# Your AWS region and S3 bucket names
AWS_REGION=us-east-2
TWINOPS_S3_BUCKET=twinops-logs
TWINOPS_FRONTEND_BUCKET=twinops-frontend

# ---- BLOCKCHAIN CONFIGURATION ----
# Polygon Mumbai RPC (Infura or Alchemy endpoint)
POLYGON_RPC=https://polygon-mumbai.infura.io/v3/

# Your wallet private key (⚠️ DO NOT SHARE or push .env)
WALLET_PRIVATE_KEY=0x<YOUR_WALLET_PRIVATE_KEY>

# The deployed contract address on Polygon Mumbai
CONTRACT_ADDRESS=0xAbCdEf1234567890abcdef1234567890abcdef12

# Relative path to your ABI file
CONTRACT_ABI_PATH=backend/abi.json

# ---- DATA PATHS ----
TECH_CSV=data/technicians.csv
TASK_CSV=data/tasks.csv

# ---- OPTIONAL AI / LLM CONFIG ----
# If using Gemini/OpenAI in the agent layer
GEMINI_API_KEY=<YOUR_GEMINI_API_KEY Not to push

# ==============================================
# ⚠️ IMPORTANT NOTES:
# 1️⃣ Do NOT commit this file as `.env` — keep it local.
# 2️⃣ Create a copy `.env` with your real keys for running.
# 3️⃣ This `.env.example` is safe to share publicly.
# ==============================================


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

