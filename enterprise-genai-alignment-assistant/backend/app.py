"""
Enterprise GenAI Assistant backend.
Includes RAG retrieval, guardrails, Ollama/Llama 3.1 generation,
reward-style scoring, and judge-agent response selection.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List

from flask import Flask, jsonify, request
from flask_cors import CORS

from llm_service import generate_policy_answer

BASE_DIR = Path(__file__).resolve().parent.parent
POLICY_FILE = BASE_DIR / "data" / "enterprise_knowledge_base.json"

app = Flask(__name__)
CORS(app)


def load_policies() -> List[Dict[str, str]]:
    with POLICY_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)["policies"]


POLICIES = load_policies()


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z]{3,}", text.lower()))


def retrieve_policies(question: str, top_k: int = 2) -> List[Dict[str, str]]:
    q_tokens = tokenize(question)
    scored = []
    for policy in POLICIES:
        combined = f"{policy['title']} {policy['owner']} {policy['content']} {' '.join(policy['keywords'])}"
        score = len(q_tokens.intersection(tokenize(combined)))
        scored.append((score, policy))
    ranked = [p for score, p in sorted(scored, key=lambda item: item[0], reverse=True) if score > 0]
    if not ranked:
        return [next(p for p in POLICIES if p["title"] == "Responsible AI Policy")]
    return ranked[:top_k]


def guardrail_check(question: str) -> Dict[str, object]:
    blocked_terms = ["password", "secret", "token", "api key", "credential", "ssn"]
    found = [term for term in blocked_terms if term in question.lower()]
    return {
        "allowed": not found,
        "signals": found,
        "message": "Sensitive data request detected." if found else "No sensitive request signal detected.",
    }


def score_candidate(answer: str) -> Dict[str, object]:
    safety_signals = ["manager approval", "coverage hours", "security", "data protection", "must not", "approved", "escalate", "do not know"]
    risk_signals = ["use your best judgment and continue", "faster", "share the data", "ignore policy", "external ai tool is fine"]
    lower = answer.lower()
    score = 50
    reasons = []
    for signal in safety_signals:
        if signal in lower:
            score += 8
            reasons.append(f"Safety/alignment signal found: '{signal}'")
    for signal in risk_signals:
        if signal in lower:
            score -= 25
            reasons.append(f"Risk signal found: '{signal}'")
    score = max(0, min(100, score))
    decision = "approved" if score >= 80 else "review" if score >= 55 else "rejected"
    return {"score": score, "decision": decision, "reasons": reasons or ["No strong signals found."]}


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "enterprise-genai-assistant"})


@app.route("/api/chat", methods=["POST"])
def chat():
    body = request.get_json(force=True) or {}
    question = (body.get("question") or "").strip()
    if not question:
        return jsonify({"error": "Question is required."}), 400

    guardrails = guardrail_check(question)
    retrieved = retrieve_policies(question)
    candidate_a = "Use your best judgment and continue if it helps complete the task faster."

    if not guardrails["allowed"]:
        candidate_b = "I cannot help expose or process secrets, credentials, tokens, or regulated personal data. Please use approved enterprise channels and escalate to Security or Responsible AI governance."
        model_status = "blocked_by_guardrail"
    else:
        candidate_b, model_status = generate_policy_answer(question, retrieved)

    score_a = score_candidate(candidate_a)
    score_b = score_candidate(candidate_b)
    selected = "Candidate B" if score_b["score"] >= score_a["score"] else "Candidate A"
    final_answer = candidate_b if selected == "Candidate B" else candidate_a

    return jsonify({
        "answer": final_answer,
        "model_status": model_status,
        "retrieved_context": retrieved,
        "guardrails": guardrails,
        "candidates": [
            {"name": "Candidate A", "type": "weak_candidate", "answer": candidate_a, "score": score_a},
            {"name": "Candidate B", "type": "real_time_llm_policy_answer", "answer": candidate_b, "score": score_b},
        ],
        "judge": {
            "selected": selected,
            "reasons": [
                "Retrieved relevant enterprise policy content.",
                "Applied responsible AI and data privacy guardrails.",
                "Generated candidate responses for comparison.",
                "Reward model scored each answer for safety, grounding, and alignment.",
                "Judge agent approved the highest-scoring enterprise-safe response.",
            ],
        },
        "phase_summary": [
            "RAG retrieves enterprise policy and guardrails check the question for data risk.",
            "Fine-tuning, PEFT, and LoRA are represented through approved enterprise answer patterns.",
            "RLHF-style reward scoring compares candidate answers and selects the safest response.",
        ],
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
