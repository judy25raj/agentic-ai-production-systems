# Atomic Agent – Azure + Elastic Observability (Logs, APM, Metrics) + Vector Search Demo

Production-style **atomic agent simulator** that runs locally or on an **Azure VM** and emits:
- ✅ **Structured JSON logs** (rotating file)
- ✅ **Elastic APM traces/transactions/spans** (optional)
- ✅ **Elastic ingest assets** (Agent config, ingest pipeline, index template)
- ✅ **Vector search / embeddings demo assets** (example scripts + workflows)

> **Safe to publish:** no credentials included. Uses `.env.example` and `.gitignore` blocks common secrets.

---

## 🏁 STATUS: PROJECT COMPLETE
**What I built:** An atomic-agent workload that produces realistic telemetry (logs + traces) and a companion set of Elastic assets that show how to ingest, parse, and observe the agent end-to-end (plus a vector-search demo starter).  
**Why it matters:** Mirrors real platform engineering concerns: standardized telemetry, correlation, and repeatable ingestion patterns that scale from a single Azure VM to fleet deployment.

---

## Key capabilities
### 1) Atomic agent simulator (Python)
- Generates realistic action events (success/failure, latency)
- Writes **structured JSON logs** to a rotating log file
- Emits **Elastic APM** transactions/spans (optional)

### 2) Elastic observability assets
- Example **Elastic Agent** configuration for log shipping
- Example **ingest pipeline** for parsing and enrichment
- Example **index template** for stable mappings

### 3) Embeddings / vector search demo (starter)
- Example scripts showing how embeddings could be generated
- Example semantic search workflow and index setup ideas

---

## Architecture
**Flow**
1. `atomic_agent.py` generates actions and telemetry  
2. Logs are written to `agent.log` (JSON)  
3. Elastic Agent ships logs → Elasticsearch ingest pipeline → logs index  
4. Elastic APM agent sends traces → APM Server → Elasticsearch → Kibana  
5. (Optional) embeddings scripts build vectors → vector index → semantic search demo

---

## Repo structure
```
atomic-agent-azure-elastic-observability/
├─ agent/
│  ├─ atomic_agent.py
│  ├─ config.yaml
│  └─ requirements.txt
├─ elastic/
│  ├─ elastic_agent_example.yml
│  ├─ ingest_pipeline.json
│  └─ index_template.json
├─ embeddings/
├─ docs/
│  └─ project_report.md
├─ .env.example
└─ .gitignore
```

---

## Quick start (local)
```bash
cd agent
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python atomic_agent.py
```

Logs will be written to the path configured in `agent/config.yaml`.

---

## Run on Azure VM (minimal)
1. Create an Azure VM (Ubuntu or Windows)
2. Install Python 3.10+
3. Clone this repo
4. Follow **Quick start (local)**
5. (Optional) Install Elastic Agent and configure it to ship `agent.log`

---

## Configuration
- `agent/config.yaml` controls agent behavior and logging
- `.env` (optional) controls Elastic APM settings

---

## Security notes
- Do not commit `.env`, tokens, SSH keys, or certificates
- This repo includes `.gitignore` and `.env.example` for safety

---

## Resume keywords
Azure • Elastic Stack • Elastic APM • Observability • Structured Logging • Ingest Pipelines • Index Templates • Tracing • Vector Search • Embeddings • Python Automation
