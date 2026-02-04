import time, random, json, uuid, datetime, requests

ES = "http://localhost:9200"
INDEX = "llm-events-demo"

def fake_llm(question):
    time.sleep(random.uniform(0.5, 1.5))
    return "Refunds are allowed within 30 days with receipt."

def fake_judge(answer):
    score = round(random.uniform(0.6, 0.95), 2)
    hallucination = score < 0.75 and random.choice([True, False])
    return score, hallucination

def send(doc):
    requests.post(f"{ES}/{INDEX}/_doc", json=doc)

def main():
    question = "What is the refund policy?"
    trace_id = str(uuid.uuid4())

    start = time.time()
    answer = fake_llm(question)
    score, hallucination = fake_judge(answer)
    latency = int((time.time() - start) * 1000)

    event = {
        "@timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "trace.id": trace_id,
        "service.name": "rag-agent-demo",
        "llm.model": "demo-llm",
        "question": question,
        "answer": answer,
        "latency_ms": latency,
        "judge.score": score,
        "judge.hallucination": hallucination,
        "tokens": random.randint(100, 300)
    }

    send(event)
    print("Sent:", event)

if __name__ == "__main__":
    main()
