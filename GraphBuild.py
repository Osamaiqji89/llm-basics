from neo4j import GraphDatabase
import os

# 1. ERSETZE DIESE PLATZHALTER MIT DEINEN AURA-ZUGANGSDATEN
NEO4J_URI = os.environ.get("NEO4J_URI")
NEO4J_BENUTZER = os.environ.get("NEO4J_USERNAME", "neo4j") # 'neo4j' als Standard
NEO4J_PASSWORT = os.environ.get("NEO4J_PASSWORD")

def add_graph_data(uri, user, password):
    driver = None
    try:
        driver = GraphDatabase.driver(uri, auth=(user, password))
        driver.verify_connectivity()
        print("--- 🎉 Verbindung erfolgreich! ---")

        with driver.session() as session:
            
            # Befehl 1: Gerät -> Fehler (Wir nutzen MERGE statt CREATE)
            # MERGE ist sicherer: Es erstellt die Daten nur, 
            # falls sie nicht schon existieren.
            cypher_1 = """
            MERGE (g:Gerät {name: 'KL2531'})
            MERGE (f:Fehler {name: 'E-12'})
            MERGE (g)-[:HAT_FEHLER]->(f)
            """
            session.run(cypher_1)
            print("Daten 'Gerät -> Fehler' sichergestellt.")

            # Befehl 2: Fehler -> Lösung (Unser neuer Befehl)
            cypher_2 = """
            MATCH (f:Fehler {name: 'E-12'})
            MERGE (l:Lösung {name: 'E-12', beschreibung: 'Gerät neu starten'})
            MERGE (f)-[:HAT_LÖSUNG]->(l)
            """
            session.run(cypher_2)
            print("Daten 'Fehler -> Lösung' sichergestellt.")
            
            print("\n--- ✅ Graph-Struktur erfolgreich erstellt! ---")

    except Exception as e:
        print(f"--- 😢 Fehler aufgetreten ---")
        print(f"Details: {e}")
        
    finally:
        if driver:
            driver.close()
            print("Verbindung geschlossen.")

# --- Skript starten ---
add_graph_data(NEO4J_URI, NEO4J_BENUTZER, NEO4J_PASSWORT)