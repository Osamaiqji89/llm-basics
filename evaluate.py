import os
from datetime import datetime
from langsmith import Client
from langchain_neo4j import Neo4jGraph, GraphCypherQAChain
from langchain_groq import ChatGroq
from langchain.smith import run_on_dataset, RunEvalConfig

# --- WICHTIG: Alle Umgebungsvariablen setzen ---
# Stelle sicher, dass GROQ_API_KEY, NEO4J_URI, NEO4J_PASSWORD,
# LANGCHAIN_TRACING_V2, LANGCHAIN_API_KEY, und LANGCHAIN_PROJECT
# in deinem Terminal gesetzt sind, bevor du das Skript startest!
# --------------------------------------------------

# --- 1. Lade den Agenten (die Kette), den wir testen wollen ---

print("Lade Graph-Assistenten (Chain)...")

# 1a. Die Graph-Brücke 🕸️
graph = Neo4jGraph(
    url=os.environ.get("NEO4J_URI"),
    username=os.environ.get("NEO4J_USERNAME", "neo4j"),
    password=os.environ.get("NEO4J_PASSWORD")
)
graph.refresh_schema() # Wichtig, damit die KI das Schema kennt

# 1b. Das Chat-Modell 🤖
llm = ChatGroq(model_name="llama-3.1-8b-instant")

# 1c. Die Kette 🔗 (Unser "Agent")
# Wir setzen verbose=True, damit LangSmith alle Zwischenschritte aufzeichnet
agent_to_test = GraphCypherQAChain.from_llm(
    graph=graph,
    llm=llm,
    verbose=True,
    allow_dangerous_requests=True  # Bestätigung, dass wir die Sicherheitsrisiken verstehen
)

# --- 2. Definiere die "Note" (Evaluierungskonfiguration) ---

# Wir sagen LangSmith, welche Noten es geben soll.
# Wir verwenden ein eigenes LLM (Groq) für die Evaluation statt OpenAI
eval_llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0)

# Gültige Evaluatoren:
# - "qa" = Question-Answering Evaluator (vergleicht Antwort mit erwarteter Antwort)
# - "cot_qa" = Chain-of-Thought QA (prüft Reasoning-Schritte)
# - "context_qa" = Context-basierte QA (prüft, ob Antwort zum Context passt)
eval_config = RunEvalConfig(
    evaluators=[
        RunEvalConfig.QA(llm=eval_llm)  # Verwende Groq LLM für die Evaluation
    ]
)

# --- 3. Starte den Testlauf ---

print("Starte Evaluation auf LangSmith...")

# Der LangSmith-Client
client = Client()

# Erstelle einen eindeutigen Projektnamen mit Zeitstempel
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
project_name = f"Graph-Eval-{timestamp}"

# Dieser Befehl automatisiert alles:
# 1. Holt dein Dataset (z.B. "graph-test-v1")
# 2. Lässt deinen 'agent_to_test' für jede Frage laufen
# 3. Wendet die 'eval_config' (unsere "Lehrer") auf die Ergebnisse an
run_results = run_on_dataset(
    client=client,
    dataset_name="graph-test-v1",  # <-- Name deines Datasets in LangSmith
    llm_or_chain_factory=agent_to_test,
    evaluation=eval_config,
    project_name=project_name  # Eindeutiger Name mit Zeitstempel
)

print("\n--- ✅ Evaluation abgeschlossen! ---")
print("Gehe jetzt in dein LangSmith-Projekt, um die Ergebnisse zu sehen.")
print(f"Test-Ergebnisse: {run_results}")