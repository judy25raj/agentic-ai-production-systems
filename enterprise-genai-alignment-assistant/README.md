# Enterprise GenAI Assistant — Real-Time Ollama + Llama 3.1

**Status: Project Complete**

A portfolio-ready enterprise GenAI demo showing a governed company-policy assistant. The application uses a Flask backend, a lightweight frontend, local Ollama with Llama 3.1, RAG-style policy retrieval, guardrails, reward-style scoring, and a judge agent decision layer.

## Business Value

This project demonstrates how an enterprise chatbot can answer policy questions safely instead of behaving like a generic chatbot. It retrieves approved policy context, checks for sensitive requests, calls a local LLM, compares candidate answers, scores them for safety and alignment, and shows transparent evidence for the final response.

## Architecture

```text
User Browser
   ↓
Frontend HTML / CSS / JavaScript
   ↓
Flask API /api/chat
   ↓
RAG-style policy retrieval from JSON knowledge base
   ↓
Guardrail check for secrets, credentials, tokens, regulated data
   ↓
Ollama API running Llama 3.1 locally
   ↓
Reward-style scoring
   ↓
Judge agent selects final enterprise-safe response
   ↓
UI displays answer + alignment evidence
```

## Concepts Demonstrated

- Prompt engineering
- RAG-style retrieval
- Responsible AI guardrails
- Real-time local LLM inference using Ollama and Llama 3.1
- Candidate answer comparison
- Reward-model-style scoring
- Judge agent decisioning
- RLHF-style alignment demonstration
- PEFT / LoRA concept represented through enterprise answer patterns and SFT examples
- Transparent alignment evidence for auditability

## Project Structure

```text
enterprise-genai-ollama-portfolio/
├── backend/
│   ├── app.py
│   └── llm_service.py
├── data/
│   ├── enterprise_knowledge_base.json
│   └── sft_examples.jsonl
├── frontend/
│   ├── app.js
│   ├── index.html
│   └── styles.css
├── .gitignore
├── README.md
└── requirements.txt
```

## Prerequisites

Install Ollama from the official Ollama website, then pull Llama 3.1:

```bash
ollama pull llama3.1
```

Start the model:

```bash
ollama run llama3.1
```

## Run the Backend

From the project root:

```bash
python -m venv .venv
```

Windows PowerShell:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Flask:

```bash
python backend/app.py
```

Backend runs at:

```text
http://127.0.0.1:5000
```

## Run the Frontend

Open this file in a browser:

```text
frontend/index.html
```

Or from the project root, run a simple static server:

```bash
python -m http.server 8000
```

Then open:

```text
http://127.0.0.1:8000/frontend/index.html
```

## Demo Questions

```text
What is our remote work policy?
```

```text
Can I share customer records with an external AI tool?
```

```text
What should I do if a request includes credentials or tokens?
```

## What Makes This Enterprise-Ready

The assistant does not only generate text. It shows the reasoning evidence needed for an enterprise demo:

1. Retrieved policy context
2. Guardrail result
3. Candidate answer comparison
4. Reward score
5. Judge agent final decision
6. Phase summary connecting RAG, Responsible AI, PEFT/LoRA concept, and RLHF-style alignment

## Important Note

This project demonstrates enterprise GenAI orchestration and alignment workflows at the application layer. It does not perform actual model fine-tuning, LoRA adapter training, or full RLHF training. PEFT, LoRA, and RLHF are represented conceptually through SFT examples, enterprise answer patterns, reward-style scoring, and judge-agent selection.

## Portfolio Summary

This project shows how a real-time local LLM can be combined with enterprise policy retrieval, guardrails, reward scoring, and judge-agent validation to produce safer and more transparent AI responses.

**Status: Project Complete**
