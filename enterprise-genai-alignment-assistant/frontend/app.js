const API_URL = "http://127.0.0.1:5000/api/chat";
const messages = document.getElementById("messages");
const form = document.getElementById("chatForm");
const input = document.getElementById("questionInput");
const evidence = document.getElementById("evidence");
const policyContext = document.getElementById("policyContext");
const scoring = document.getElementById("scoring");
const judgeDecision = document.getElementById("judgeDecision");

function escapeHtml(text) {
  return String(text).replace(/[&<>"]/g, (ch) => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;"}[ch]));
}

function addMessage(role, text) {
  const div = document.createElement("div");
  div.className = `message ${role}`;
  div.innerHTML = `<strong>${role === "user" ? "You" : "Enterprise Assistant"}</strong><p>${escapeHtml(text)}</p>`;
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

function renderEvidence(data) {
  evidence.classList.remove("hidden");
  policyContext.innerHTML = data.retrieved_context.map(p => `
    <div class="policy-box">
      <h3>${escapeHtml(p.title)}</h3>
      <small>${escapeHtml(p.owner)}</small>
      <p>${escapeHtml(p.content)}</p>
    </div>`).join("");

  scoring.innerHTML = data.candidates.map(c => {
    const decision = c.score.decision;
    return `<div class="score-box">
      <h3>${escapeHtml(c.name)} — ${escapeHtml(c.type)}</h3>
      <p>${escapeHtml(c.answer)}</p>
      <span class="score-pill ${decision}">Score: ${c.score.score}/100 • ${decision}</span>
      <ul>${c.score.reasons.map(r => `<li>${escapeHtml(r)}</li>`).join("")}</ul>
    </div>`;
  }).join("");

  judgeDecision.innerHTML = `<div class="judge-box">
    <h3>Selected response: ${escapeHtml(data.judge.selected)}</h3>
    <ul>${data.judge.reasons.map(r => `<li>${escapeHtml(r)}</li>`).join("")}</ul>
    <h3>Phase summary</h3>
    <ul>${data.phase_summary.map(r => `<li>${escapeHtml(r)}</li>`).join("")}</ul>
  </div>`;
}

async function ask(question) {
  addMessage("user", question);
  addMessage("assistant", "Thinking through RAG, guardrails, Llama 3.1, reward scoring, and judge selection...");
  const loading = messages.lastChild;

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Backend error");
    loading.querySelector("p").textContent = data.answer;
    renderEvidence(data);
  } catch (err) {
    loading.querySelector("p").textContent = `Error: ${err.message}. Make sure Flask is running on port 5000.`;
  }
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const question = input.value.trim();
  if (!question) return;
  input.value = "";
  ask(question);
});

document.querySelectorAll(".chips button").forEach(btn => {
  btn.addEventListener("click", () => ask(btn.dataset.question));
});

document.getElementById("clearBtn").addEventListener("click", () => {
  messages.innerHTML = `<div class="message assistant"><strong>Enterprise Assistant</strong><p>Hello. Ask me a company-policy question and I will answer using a governed GenAI flow.</p></div>`;
  evidence.classList.add("hidden");
});
