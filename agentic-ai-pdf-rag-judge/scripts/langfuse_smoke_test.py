import os

try:
    from dotenv import load_dotenv
    load_dotenv()  # loads .env if present (ignored by git)
except Exception:
    pass


def main() -> int:
    host = os.getenv("LANGFUSE_HOST", "").strip()
    if host:
        print(f"LANGFUSE_HOST set: {host}")
    else:
        print("LANGFUSE_HOST not set (ok if using default).")

    # Fail fast if keys are missing
    pub = os.getenv("LANGFUSE_PUBLIC_KEY")
    sec = os.getenv("LANGFUSE_SECRET_KEY")
    if not pub or not sec:
        print("❌ Missing LANGFUSE_PUBLIC_KEY / LANGFUSE_SECRET_KEY in environment.")
        print("   Copy .env.example -> .env and set values.")
        return 1

    try:
        # v3 client style (newer)
        from langfuse import get_client

        client = get_client()
        trace = client.trace(name="smoke_test", input={"ok": True})
        trace.update(output={"done": True})
        print(f"✅ Langfuse smoke test succeeded (v3). Trace ID: {getattr(trace, 'id', None)}")
        return 0

    except Exception as e_v3:
        # fallback for older SDK style
        try:
            from langfuse import Langfuse

            lf = Langfuse()
            span = lf.span.create(name="smoke_test", input={"ok": True})
            trace_id = getattr(span, "trace_id", getattr(span, "id", None))
            print(f"✅ Langfuse smoke test succeeded (v2). Trace/Span ID: {trace_id}")
            return 0

        except Exception as e_v2:
            print("❌ Langfuse smoke test failed.")
            print(f"   v3 error: {e_v3}")
            print(f"   v2 error: {e_v2}")
            return 2


if __name__ == "__main__":
    raise SystemExit(main())
