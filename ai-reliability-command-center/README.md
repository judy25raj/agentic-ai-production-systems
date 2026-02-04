# 🧠 Agentic AI — Reliability Command Center (ELK Observability)

🏁 **STATUS: PROJECT COMPLETE**  
This project is finalized and maintained for portfolio and demonstration purposes.

This project demonstrates a production-style AI observability platform that monitors agent behavior in real time using the Elastic Stack (Elasticsearch + Kibana).

It brings SRE-style monitoring to LLM and agentic AI systems by tracking:

- ⏱️ Latency  
- ⭐ Response quality (Judge score)  
- 🚨 Hallucination risk  
- 💸 Token usage  
- 🔗 Trace correlation  

---

## 🔍 What the System Does

Emits structured telemetry from an AI agent and a Judge Agent into Elasticsearch, then visualizes reliability signals in Kibana dashboards.

---

## 🔁 Pipeline Flow

AI Agent → Judge Agent → Telemetry JSON → Elasticsearch → Kibana Dashboards

---

## 📊 Captured Signals

| Field | Meaning |
|------|---------|
| latency_ms | Performance |
| judge.score | Response quality |
| judge.hallucination | Risk flag |
| tokens | Cost proxy |
| trace.id | Correlation ID |

---

## 🧰 Tech Stack

- Python 3.10+
- Elasticsearch 8.x
- Kibana (Lens Dashboards)
- Docker + Docker Compose
- requests (HTTP telemetry)

---

## ⚡ Quick Start

```bash
docker compose up -d
pip install requests
python demo_ai.py
```

Open Kibana: http://localhost:5601

Create Data View:

- **Name:** llm-events-demo  
- **Time field:** @timestamp  

---

## 📈 Dashboards

- **Avg AI Latency (ms)** – Monitors response time  
- **Avg AI Quality** – Tracks reliability  
- **Hallucinations Detected** – Flags unsafe responses  

---

## 📂 Repository Layout

```
ai-reliability-command-center/
├── demo_ai.py
├── docker-compose.yml
├── screenshots/
└── README.md
```

---

## 🔎 Useful Filters (KQL)

```kql
judge.hallucination : true
latency_ms > 1500
judge.score < 0.75
```

---

## 📝 Notes

- This project does not use external web search  
- Telemetry is structured JSON for production-style observability  
- Designed for portfolio use: clean, repeatable, no private data  
- Mirrors real-world AI reliability monitoring patterns  
