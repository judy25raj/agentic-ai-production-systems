# Atomic Agent – Azure + Elastic Observability

A **production-style observability project** that demonstrates how a lightweight *Atomic Agent* running on an **Azure VM** can emit system metrics, structured logs, and traces into **Elastic Stack**, enabling real-time monitoring through **Kibana dashboards**.

This project is designed as a **portfolio-grade example** aligned with **Agentic AI**, **Platform Engineering**, and **Cloud Observability** best practices.

---

## 🚀 Project Overview

The Atomic Agent runs as a Python process on an Azure Linux VM and periodically emits:

- Host-level system metrics (CPU, memory, disk)
- Structured JSON logs
- Heartbeat-style operational signals

These signals flow through Elastic ingest pipelines into Elasticsearch indices and are visualized using Kibana’s Observability and Infrastructure views.

---

## 🏗 Architecture

![Architecture](screenshots/architecture.png)

**Flow:**

Azure VM  
→ Atomic Agent (Python)  
→ Elastic Ingest Pipeline  
→ Elasticsearch Index  
→ Kibana (Discover, Dashboards, Infrastructure)

---

## 🔍 What This Project Demonstrates

- Azure VM provisioning and secure SSH access
- Custom agent-based telemetry generation
- Structured logging with parsed fields
- Elastic Observability (Logs, Metrics, Infrastructure)
- Kibana dashboards built from real telemetry
- Production-style folder and README structure

---

## 📊 Observability Evidence

### Azure VM Infrastructure Metrics
![Infrastructure Hosts](screenshots/infrastructure_hosts.png)

Shows real-time CPU, memory, and disk utilization for the Azure VM host as detected by Elastic Infrastructure monitoring.

---

### Parsed Logs in Kibana Discover
![Parsed Logs](screenshots/kibana-discover-parsed-logs.jpg)

Demonstrates structured logs emitted by the Atomic Agent, including custom fields such as CPU, memory, disk usage, and embeddings metadata.

---

### Kibana Observability Dashboard
![Observability Dashboard](screenshots/kibana-observability-dashboard.jpg)

A custom dashboard visualizing:
- CPU utilization trends
- Memory consumption
- Disk usage
- Log volume over time

---

## 🧠 Why This Matters (Portfolio Value)

This project goes beyond basic logging by showing:

- Agent-style telemetry instead of platform defaults
- Clean separation of ingestion, indexing, and visualization
- Cloud-native observability aligned with real SRE workflows
- Skills relevant to **Platform Engineering**, **Cloud Infra**, and **Agentic AI systems**

Recruiters can clearly see **how data flows**, **how it’s structured**, and **how it’s operationalized**.

---

## 🛠 Tech Stack

- **Cloud:** Azure VM (Linux)
- **Language:** Python
- **Observability:** Elastic Stack (Elasticsearch, Kibana)
- **Logging & Metrics:** Custom Atomic Agent
- **Dashboards:** Kibana Observability & Infrastructure

---

## 📁 Repository Structure

```
atomic-agent-azure-elastic-observability/
├── screenshots/
│   ├── architecture.png
│   ├── infrastructure_hosts.png
│   ├── kibana-discover-parsed-logs.jpg
│   └── kibana-observability-dashboard.jpg
├── README.md
└── .gitkeep
```

---

## ✅ Status

**Project Status:** ✅ Complete  
**Use Case:** Portfolio / Demonstration / Interview-ready

---

## 📌 Resume-Ready Summary

> Built a production-style Azure observability pipeline using a custom Python-based Atomic Agent, Elastic ingest pipelines, and Kibana dashboards to monitor real-time VM metrics and structured logs.

---

If you’d like:
- Terraform version  
- Agent-as-a-service design  
- A follow-up Agentic AI project  

Just say the word 🚀
