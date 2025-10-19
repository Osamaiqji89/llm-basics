import os
from langchain_neo4j import Neo4jGraph, GraphCypherQAChain
from langchain_groq import ChatGroq

# --- VORBEREITUNG (Stelle sicher, dass die API-Schlüssel gesetzt sind) ---

# 1. ERSETZE DIESE PLATZHALTER
NEO4J_URI = os.environ.get("NEO4J_URI")
NEO4J_BENUTZER = os.environ.get("NEO4J_USERNAME", "neo4j") # 'neo4j' als Standard
NEO4J_PASSWORT = os.environ.get("NEO4J_PASSWORD")

if "GROQ_API_KEY" not in os.environ:
    print("Fehler: GROQ_API_KEY nicht gefunden.")
    print("Bitte setze die Umgebungsvariable, z.B.:")
    exit()

# --- 1. SETUP (Modelle und DB laden) ---

try:
    print("Verbinde LangChain mit Neo4j...")
    # 1a. Die Graph-Brücke 🕸️
    graph = Neo4jGraph(
        url=NEO4J_URI,
        username=NEO4J_BENUTZER,
        password=NEO4J_PASSWORT
    )
    # Schema einlesen (damit die KI weiß, wie der Graph gebaut ist)
    graph.refresh_schema()
    print("Schema der Datenbank erfolgreich gelesen.")

    # 1b. Das Chat-Modell 🤖
    llm = ChatGroq(model_name="llama-3.1-8b-instant")

    # 1c. Die Kette 🔗 (Die Logik, die alles verbindet)
    chain = GraphCypherQAChain.from_llm(
        graph=graph,  # Unser Graph-Objekt
        llm=llm,      # Unser Chat-Modell
        verbose=True,  # Setze dies auf True, um die Cypher-Abfrage zu sehen!
        allow_dangerous_requests=True  # Bestätigung, dass wir die Sicherheitsrisiken verstehen
    )
    print("GraphCypherQAChain erfolgreich erstellt.")


    # --- 2. FRAGE STELLEN (Hier passiert der .invoke()) ---
    
    frage = "Wie löse ich Gerät KL2531 Fehler E-12?"
    print(f"\nStelle die Frage an die Kette: '{frage}'")

    # Hier rufen wir die Kette auf:
    antwort = chain.invoke(frage)

    # --- 3. ANTWORT ANZEIGEN ---
    print("\n--- Antwort vom Assistenten ---")
    print(antwort.get('result', 'Keine Antwort erhalten.'))
    print("---------------------------------")


except Exception as e:
    print(f"--- 😢 Ein Fehler ist aufgetreten ---")
    print(f"Details: {e}")