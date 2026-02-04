🧠 Agentic AI — Reliability Command Center (ELK Observability)

🏁 STATUS: PROJECT COMPLETE
This project is finalized and maintained for portfolio and demonstration purposes.

This project demonstrates a production-style AI observability platform that monitors agent behavior in real time using the Elastic Stack (Elasticsearch + Kibana).

It brings SRE-style monitoring to LLM and agentic AI systems by tracking:

Latency

Response quality (Judge score)

Hallucination risk

Token usage

Trace correlation

What the System Does

Emits structured telemetry from an AI agent and judge agent into Elasticsearch, then visualizes reliability signals in Kibana.

Pipeline Flow

AI Agent → Judge Agent → Telemetry JSON → Elasticsearch → Kibana Dashboards

Captured Signals

latency_ms → performance

judge.score → quality

judge.hallucination → risk

tokens → cost proxy

trace.id → correlation

Tech Stack

Python 3.10+

Elasticsearch 8.x

Kibana (Lens Dashboards)

Docker + Docker Compose

requests (HTTP telemetry)

Quick Start
1) Start ELK
docker compose up -d

2) Install dependencies
pip install requests

3) Generate observability events
python demo_ai.py


Run multiple times to populate the dashboards.

4) Open Kibana
http://localhost:5601


Create a data view:

Name: llm-events-demo

Time field: @timestamp

Dashboards
Panel	Description
Avg AI Latency (ms)	Monitors response time
Avg AI Quality (Judge Score)	Tracks reliability
Hallucinations Detected	Flags unsafe responses
Repository Layout
ai-reliability-command-center/
├── demo_ai.py                # Agent + Judge + telemetry
├── docker-compose.yml       # Elasticsearch + Kibana
├── screenshots/             # Dashboard images
└── README.md

Useful Filters (KQL)

Show hallucinations:

judge.hallucination : true


Slow responses:

latency_ms > 1500


Low quality:

judge.score < 0.75

Notes

This project does not use external web search

Telemetry is structured JSON for production-style observability

Designed for portfolio use: clean, repeatable, no private data

Mirrors real-world AI reliability monitoring patterns
