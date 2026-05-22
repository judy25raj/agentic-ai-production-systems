"""
LLM service layer for the Enterprise GenAI Assistant.
Connects Flask to Ollama / Llama 3.1 running locally.
"""
from __future__ import annotations

import os
from typing import Dict, List, Tuple

import requests

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1")
TIMEOUT_SECONDS = int(os.getenv("OLLAMA_TIMEOUT_SECONDS", "60"))


def build_enterprise_prompt(question: str, policies: List[Dict[str, str]]) -> str:
    policy_text = "\n\n".join(
        f"Policy: {p['title']}\nOwner: {p['owner']}\nContent: {p['content']}"
        for p in policies
    )
    return f"""
You are an enterprise policy assistant.
Answer only from the approved policy context below.
Do not invent facts. If the policy is missing, say you do not know and recommend escalation.
Keep the answer professional, safe, and concise.

Approved policy context:
{policy_text}

User question:
{question}

Enterprise answer:
""".strip()


def call_ollama(prompt: str) -> Tuple[str, str]:
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.2, "top_p": 0.9, "num_predict": 300},
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=TIMEOUT_SECONDS)
        response.raise_for_status()
        data = response.json()
        answer = (data.get("response") or "").strip()
        if not answer:
            return "I could not generate an answer from the local model.", "empty_model_response"
        return answer, f"ollama:{OLLAMA_MODEL}"
    except requests.exceptions.ConnectionError:
        return (
            "The local Ollama service is not reachable. Start Ollama and run: ollama run llama3.1",
            "ollama_connection_error",
        )
    except requests.exceptions.Timeout:
        return "The local Llama 3.1 model timed out. Please try again.", "ollama_timeout"
    except Exception as exc:
        return f"LLM service error: {exc}", "ollama_error"


def generate_policy_answer(question: str, policies: List[Dict[str, str]]) -> Tuple[str, str]:
    prompt = build_enterprise_prompt(question, policies)
    return call_ollama(prompt)
