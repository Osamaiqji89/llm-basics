from neo4j import GraphDatabase
import os

# 1. ERSETZE DIESE PLATZHALTER MIT DEINEN AURA-ZUGANGSDATEN
NEO4J_URI = os.environ.get("NEO4J_URI")
NEO4J_BENUTZER = os.environ.get("NEO4J_USERNAME", "neo4j") # 'neo4j' als Standard
NEO4J_PASSWORT = os.environ.get("NEO4J_PASSWORD")

# Diese Funktion prüft die Verbindung
def check_connection(uri, user, password):
    driver = None
    try:
        # Versucht, eine Verbindung (Driver-Objekt) herzustellen
        driver = GraphDatabase.driver(uri, auth=(user, password))
        
        # Prüft, ob die Zugangsdaten gültig sind
        driver.verify_connectivity()
        print("--- 🎉 Verbindung zur Neo4j Aura Datenbank erfolgreich! ---")
        
        # Testet eine einfache Abfrage
        with driver.session() as session:
            result = session.run("RETURN 'Test erfolgreich' AS message")
            print(f"Abfrage-Ergebnis: {result.single()['message']}")
            
    except Exception as e:
        print(f"--- 😢 Verbindung fehlgeschlagen ---")
        print(f"Fehlerdetails: {e}")
        
    finally:
        # Wichtig: Immer die Verbindung schließen
        if driver:
            driver.close()
            print("\nVerbindung geschlossen.")

# --- Skript starten ---
check_connection(NEO4J_URI, NEO4J_BENUTZER, NEO4J_PASSWORT)