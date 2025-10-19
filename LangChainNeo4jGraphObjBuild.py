from langchain_neo4j import Neo4jGraph
import os

# 1. ERSETZE DIESE PLATZHALTER
NEO4J_URI = os.environ.get("NEO4J_URI")
NEO4J_BENUTZER = os.environ.get("NEO4J_USERNAME", "neo4j") # 'neo4j' als Standard
NEO4J_PASSWORT = os.environ.get("NEO4J_PASSWORD")

# --- RAG-Projekt START ---

print("Verbinde LangChain mit Neo4j...")
try:
    # Dies ist die LangChain-Brücke zu unserer Datenbank
    graph = Neo4jGraph(
        url=NEO4J_URI,
        username=NEO4J_BENUTZER,
        password=NEO4J_PASSWORT
    )
    
    # Wir können das Schema (unsere Ontologie) automatisch auslesen lassen
    graph.refresh_schema()
    
    print("\n--- Schema der Datenbank erfolgreich gelesen: ---")
    print(graph.schema)
    print("-------------------------------------------------")

except Exception as e:
    print(f"--- 😢 Verbindung fehlgeschlagen ---")
    print(f"Details: {e}")