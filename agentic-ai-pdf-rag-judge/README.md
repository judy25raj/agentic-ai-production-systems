# Agentic AI — PDF RAG + Judge Agent (with Optional Langfuse)

This project demonstrates a **production-style agentic RAG pipeline** designed to generate
**grounded answers from documents** and validate response quality using a Judge Agent.

## What the Pipeline Does
- Ingests PDFs → chunks text → builds a local embedding index
- Retrieves the most relevant chunks for a given question
- Generates a grounded answer using an LLM (Groq)
- Evaluates the answer with a Judge Agent and produces a scored report
- Optionally sends traces and spans to **Langfuse** for observability

✅ Designed for portfolio use: clean structure, repeatable scripts, and no bundled private data.
