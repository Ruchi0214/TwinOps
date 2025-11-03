# 🌐 TwinOps.AI  
### Smart Technician Assignment with AI + AWS + Blockchain Audit  

> **Tagline:** Automating MSP operations with intelligent technician dispatch and verifiable blockchain audit trails.  
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
TwinOps Web App (Next.js + React)
        ↓
FastAPI Backend (EC2)
        ↓
Amazon Bedrock Agent (Gemini + LangChain + PyTorch logic)
        ↓
 ┌──────────────────────────────┬──────────────────────────────┬──────────────────────────────┐
 | 🧠 Task Agent                | 🔒 Audit Agent               | 💬 Support Agent               |                         
 | (Bedrock)                    | (S3 + Polygon Blockchain)    |          (Gemini )           |
 └──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
        ↓
AWS S3 (Logs & Data) + PostgreSQL / MongoDB (Persistent Storage)
        ↓
Polygon Blockchain (Immutable Audit Trail & Smart Contract Logging)
        ↓
AWS CloudWatch (Monitoring + Observability Dashboard)


*Cloud-native, event-driven, and modular.*

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
```git clone https://github.com/Ruchi0214/TwinOps.git
cd TwinOps/backend

2️⃣ Create Python Environment
