# 🚀 HealStack AI

<div align="center">

### **AI-Powered Self-Healing Infrastructure & Incident Management Platform**

*Enterprise-Grade AIOps • Predictive Monitoring • Intelligent Incident Management • Autonomous Remediation*

[![Python Version](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)](https://www.sqlalchemy.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

</div>

---

## 📖 Overview

**HealStack AI** is an enterprise-grade, AI-powered infrastructure monitoring and self-healing platform. It is engineered to proactively detect, analyze, predict, and resolve system anomalies and failures before they affect end-users.

Traditional monitoring systems are **reactive**—notifying engineers only after service degradation occurs. HealStack AI shifts the paradigm to **proactive and autonomous operations** by unifying:

* 📊 **Real-Time Infrastructure Monitoring** (System metrics & process health)
* 🧠 **Intelligent Incident Detection** (Resource bottleneck & anomaly detection)
* 🔍 **AI-Powered Root Cause Analysis (RCA)** (LLM & ML-assisted diagnostics)
* 📈 **Predictive Failure Detection** (Forecasting metric spikes & resource exhaustion)
* ⚡ **Automated Remediation** (Autonomous recovery actions and custom playbooks)
* 🔗 **Blockchain-Backed Audit Logs** (Immutable incident tracking & compliance)

---

## 🎯 Problem Statement

Modern microservice and cloud infrastructures generate millions of metrics, thousands of logs, and hundreds of daily alerts. Operations teams suffer from:

* **Alert Fatigue:** Bombardment of low-priority alerts masking critical failures.
* **High MTTR (Mean Time to Recovery):** Slow manual correlation of logs, metrics, and codebases.
* **Operational Inefficiencies:** Recurring issues requiring manual restarts and repetitive interventions.
* **Loss of Revenue & SLA Breaches:** Delayed resolution directly impacting system availability.

**HealStack AI** automates this lifecycle by analyzing system telemetry, identifying root causes, and executing safe, verified self-healing workflows automatically.

---

## ✨ Key Features

| Feature Domain | Capabilities |
| :--- | :--- |
| **Telemetry & Monitoring** | Real-time monitoring of CPU utilization, Memory pressure, Disk I/O & saturation, running processes, and service port availability. |
| **Intelligent Anomaly Detection** | Rule-based and statistical detection of memory leaks, CPU spikes, disk saturation, and hanging services. |
| **Incident Lifecycle Management** | Automated incident creation, dynamic severity classification, status workflow tracking, and historical audit trails. |
| **AI/ML Diagnostics** | Out-of-the-box support for OpenAI GPT models and local Ollama deployments to analyze telemetry context and generate Root Cause Analyses (RCA). |
| **Autonomous Remediation** | Self-healing engine capable of executing container restarts, clearing temp caches, resizing resources, and triggering recovery webhooks. |
| **Blockchain Audit Trail** | Recording incident reports and remediation steps on a distributed ledger to guarantee complete compliance and security logs. |

---

## 🏗 System Architecture

```text
                                  ┌──────────────────────┐
                                  │      Dashboard       │
                                  │   (Next.js WebApp)   │
                                  └──────────┬───────────┘
                                             │
                                             ▼
                                  ┌──────────────────────┐
                                  │     FastAPI API      │
                                  │   (Backend Engine)   │
                                  └──────────┬───────────┘
                                             │
         ┌───────────────────────────────────┼───────────────────────────────────┐
         ▼                                   ▼                                   ▼
┌──────────────────┐               ┌──────────────────┐               ┌──────────────────┐
│  Monitoring Core │               │  Incident Agent  │               │   AI/ML Engine   │
│  (psutil & Prom) │               │   (Lifecycle)    │               │  (RCA & Predict) │
└────────┬─────────┘               └────────┬─────────┘               └────────┬─────────┘
         │                                  │                                  │
         ▼                                  ▼                                  ▼
┌──────────────────┐               ┌──────────────────┐               ┌──────────────────┐
│    Metrics DB    │               │  Relational DB   │               │    ML Models     │
│   (Prometheus)   │               │   (PostgreSQL)   │               │ (Scikit / LLMs)  │
└──────────────────┘               └────────┬─────────┘               └──────────────────┘
                                            │
                                            ▼
                               ┌──────────────────────────┐
                               │   Self-Healing Engine    │
                               │   (Automated Playbooks)  │
                               └────────────┬─────────────┘
                                            │
                                            ▼
                               ┌──────────────────────────┐
                               │   Infrastructure Layer   │
                               │  (Docker / VM Services)  │
                               └──────────────────────────┘
```

---

## 📂 Project Structure

```bash
healstack-ai/
├── backend/                    # FastAPI Backend Application
│   ├── app/
│   │   ├── api/                # API Route Controllers (e.g., incidents, health)
│   │   ├── core/               # Configuration, DB Setup, & Security settings
│   │   ├── models/             # SQLAlchemy ORM Models
│   │   ├── schemas/            # Pydantic Schemas for validation
│   │   ├── services/           # Incident and Remediation services
│   │   ├── monitoring/         # Telemetry collectors and detector logic
│   │   ├── utils/              # Helper utilities
│   │   └── main.py             # FastAPI entrypoint
├── frontend/                   # Dashboard Web Interface (Next.js Application)
│   └── src/
│       ├── app/                # Pages and Routing
│       ├── components/         # Reusable UI Elements (UI/UX Layer)
│       ├── hooks/              # Custom React hooks
│       ├── lib/                # Client configurations
│       └── services/           # Backend API integration clients
├── ai-engine/                  # Machine Learning & AI Modeling
│   ├── datasets/               # Training data and telemetry logs
│   ├── models/                 # Serialized models and LLM configuration
│   └── training/               # Model training scripts
├── blockchain/                 # Immutable Ledger Audit Logging
│   ├── contracts/              # Smart contracts (Solidity/Vyper)
│   └── scripts/                # Migration and deployment scripts
├── infrastructure/             # Containerization & Deployment configs
│   ├── docker/                 # Service Dockerfiles
│   └── nginx/                  # Reverse proxy configurations
├── monitoring/                 # Observability Stack setup
│   ├── grafana/                # Grafana dashboards configurations
│   └── prometheus/             # Prometheus scrape target rules
├── docker-compose.yml          # Local multi-container environment launcher
├── test_metrics.py             # Collector validation script
├── .env                        # Configuration environment variables
└── README.md                   # Project Documentation
```

---

## ⚙️ Installation & Setup

### Prerequisites
* Python 3.11+
* Node.js v18+ (for frontend dashboard)
* Docker & Docker Compose
* PostgreSQL (or SQLite for development)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/healstack-ai.git
cd healstack-ai
```

### 2. Set Up Environment Variables
Create a `.env` file in the root directory:
```env
PROJECT_NAME="HealStack AI"
PROJECT_VERSION="1.0.0"

# Backend server config
BACKEND_HOST=127.0.0.1
BACKEND_PORT=8000

# Database Configuration (SQLite default for dev)
DATABASE_URL=sqlite:///./healstack.db

# LLM Providers for AI Engine
OPENAI_API_KEY=your-openai-api-key
OLLAMA_BASE_URL=http://localhost:11434

# Security settings
SECRET_KEY=your_super_secure_secret_key_change_in_prod
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3. Spin Up Services using Docker
To start the database and required background tools:
```bash
docker-compose up -d
```

### 4. Running the Backend (FastAPI)
Create and activate your virtual environment, install requirements, and run the backend:
```bash
# Create and activate environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r backend/requirements.txt  # Alternatively: pip install fastapi uvicorn sqlalchemy psutil pydantic

# Run the app
uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```
* **API Swagger Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc Documentation:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 5. Running the Frontend (Next.js Dashboard)
```bash
cd frontend
npm install
npm run dev
```
* **Dashboard Access:** [http://localhost:3000](http://localhost:3000)

---

## 📊 Telemetry & Anomaly Processing

### Live System Telemetry Payload
The monitoring engine fetches active host resource usages in the following JSON schema:
```json
{
  "cpu_usage": 14.5,
  "memory_usage": 68.2,
  "disk_usage": 45.1,
  "timestamp": "2026-06-02T12:51:00.827601"
}
```

### Anomaly Detection & Incident Pipeline
If usage crosses pre-configured thresholds (e.g., CPU > 90% or Memory > 85%), HealStack AI logs the anomaly:
```json
[
  {
    "type": "CPU",
    "value": 92.4,
    "severity": "HIGH",
    "message": "CPU usage exceeded threshold"
  }
]
```
The state machine automatically flags an Incident through the lifecycle:

```text
  [Detected] ──► [Open] ──► [Investigating] ──► [Resolved] ──► [Closed]
```

---

## 📈 Development Roadmap

### **Phase 1 — Foundation Layer** (Current)
* [x] FastAPI Core Server Setup
* [x] SQLAlchemy Database Models for Incidents
* [x] Live System Telemetry Engine (psutil Integration)
* [x] Threshold-based Issue Detection Rules
* [x] Interactive API Swagger Docs
* [ ] Full Metrics API endpoints
* [ ] Next.js Frontend Dashboard Integration

### **Phase 2 — Incident Intelligence**
* [ ] Alert Management Dispatcher
* [ ] Automated Integrations (Email, Slack webhooks, PagerDuty)
* [ ] Real-time WebSocket connection to Dashboard
* [ ] Core Root Cause Analysis (RCA) Engine

### **Phase 3 — Predictive AI**
* [ ] Historical telemetry database archiving (Time-scale / Prometheus)
* [ ] ML Anomaly Detection model (Scikit-Learn Isolation Forests)
* [ ] Resource exhaust prediction algorithms

### **Phase 4 — Autonomous Remediation**
* [ ] Automated recovery playbooks definition (YAML configurations)
* [ ] Self-Healing Engine (Service restarts, cache purges, container re-spins)
* [ ] Verification checks after executing healing scripts

---

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 👨‍💻 Author

### **Kumar Sambhav**
*B.Tech in Computer Science & Engineering*
* AI/ML Enthusiast • Backend Developer • Future AIOps Engineer
* [GitHub Profile](https://github.com/KumarSambhav01)

---
<div align="center">
⭐ If you find HealStack AI useful or plan to build upon it, please consider giving the repository a star!
</div>
