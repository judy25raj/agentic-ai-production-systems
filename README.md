# ⭐ Agentic AI Systems & Cloud Observability
**Author:** Judy Raj

This repository contains production-style Agentic AI and Cloud Observability systems that demonstrate how modern AI platforms can be:

- Grounded
- Evaluated
- Observable
- Operationally reliable

These are engineering systems, not demos.  
They follow real-world practices used in regulated, enterprise, and AI-first environments.

## 🧠 What This Portfolio Demonstrates
- Agentic AI workflows (multi-agent orchestration)
- Retrieval-Augmented Generation (RAG)
- Automated evaluation using Judge Agents
- AI reliability & hallucination detection
- Cloud-native deployment on Azure
- Observability-first system design (logs, metrics, traces)
- Secure configuration & production hygiene
- Interview-ready documentation and structure

## 📌 Featured Projects

### 🔹 Project 1: Agentic AI — PDF RAG + Judge Agent
📁 Folder: agentic-ai-pdf-rag-judge

**Architecture Flow**  
PDFs → Retriever Agent → Generator Agent → Judge Agent → JSON Report  
(Optional) Langfuse → Observability

**Status:** ✅ Complete

---

### 🔹 Project 2: Agentic AI — Reliability Command Center (ELK Observability)
📁 Folder: ai-reliability-command-center

**Architecture Flow**  
AI Agent → Judge Agent → Telemetry JSON → Elasticsearch → Kibana Dashboards

| Field | Meaning |
|------|---------|
| latency_ms | Performance |
| judge.score | Response quality |
| judge.hallucination | Risk flag |
| tokens | Cost proxy |
| trace.id | Correlation |

**Status:** ✅ Complete

---

### 🔹 Project 3: Atomic Agent on Azure with Elastic Observability
📁 Folder: atomic-agent-azure-elastic-observability

**Architecture Flow**  
Atomic Agent → Elastic → Elasticsearch → Kibana

**Status:** ✅ Complete

---

## 📁 Repository Structure
```
agentic-ai-production-systems/
├── agentic-ai-pdf-rag-judge/
├── ai-reliability-command-center/
├── atomic-agent-azure-elastic-observability/
├── .gitignore
└── README.md
```

## 🔐 Security & Configuration
- Sensitive values are never committed
- Environment variables via .env
- .env.example templates included
- .gitignore enforces safe practices

## 👩‍💻 About the Author
Judy Raj — Senior Platform & Automation Engineer  
Focused on trustworthy, observable, production-grade AI systems.
