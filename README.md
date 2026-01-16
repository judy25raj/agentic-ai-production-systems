# ⭐ Agentic AI Systems & Cloud Observability

**Author: Judy Raj**

This repository contains **production-style Agentic AI systems**
demonstrating how **Retrieval-Augmented Generation (RAG)**, multi-agent
workflows, evaluation, and **cloud observability** can be combined to
build reliable, debuggable AI applications.

The focus is on **real-world engineering practices**: clear agent
responsibilities, structured outputs, quality checks, and operational
visibility.

------------------------------------------------------------------------

## 🧠 Featured Project 1 --- Agentic AI: PDF RAG with Judge Agent

### Problem Addressed

LLM-based systems require **grounded responses and quality validation**.
This project demonstrates how multiple AI agents collaborate to ensure
accuracy, relevance, and traceability when answering questions from
documents.

### Architecture Flow

1.  PDF documents are ingested and chunked
2.  A retrieval agent performs vector-based semantic search
3.  A generation agent produces a response using retrieved context
4.  A judge agent evaluates response quality and relevance
5.  Structured JSON output is produced for traceability and scoring

*(Architecture diagram available in the `architecture/` folder.)*

### Key Capabilities

-   Multi-agent workflow (Retriever → Generator → Judge)
-   PDF ingestion with vector embeddings
-   LLM-driven response generation
-   Automated evaluation and scoring
-   Deterministic, structured outputs

### Skills & Technologies

**Python · Agentic AI · RAG · Vector Embeddings · AI Evaluation · Prompt
Engineering**

📁 Folder: `agentic-ai-pdf-rag-judge`

------------------------------------------------------------------------

## ☁️ Featured Project 2 --- Atomic Agent on Azure with Elastic Observability

### Problem Addressed

AI agents running in production must be **observable, debuggable, and
auditable**. This project focuses on **operational visibility** rather
than model accuracy alone.

### Architecture Flow

1.  Atomic AI agent executes a defined task
2.  Execution logs and metrics are generated
3.  Data is shipped to the Elastic Stack
4.  Dashboards provide runtime visibility and trace analysis

### Key Capabilities

-   Atomic agent execution model
-   Azure VM--based deployment
-   Centralized logging and metrics
-   Observability dashboards
-   Operational monitoring for distributed systems

### Skills & Technologies

**Azure · Elastic Stack · Observability · Cloud Operations ·
Automation**

📁 Folder: `atomic-agent-azure-elastic-observability`

------------------------------------------------------------------------

## ▶️ How to Run (Example)

``` bash
pip install -r requirements.txt
python main.py
```

Each project folder contains additional setup instructions.

------------------------------------------------------------------------

## 👩‍💻 About

Senior Platform & Automation Engineer with extensive experience in
enterprise application development, automation, and production support.
Currently focused on **Agentic AI systems, AI evaluation frameworks,
Python automation, and cloud observability** in regulated environments.

This repository reflects **implementation-focused engineering work**
rather than academic demonstrations.

------------------------------------------------------------------------

## 📌 Notes

-   Sensitive configuration values are excluded
-   Environment variables are managed using `.env.example`
-   Each project folder contains a detailed README
-   Designs are extensible and production-aligned
