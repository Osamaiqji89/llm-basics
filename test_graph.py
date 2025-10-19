import os
from neo4j import GraphDatabase

# WICHTIG: Dieser Test braucht die exakt gleichen 
# Umgebungsvariablen wie unser Haupt-Skript!
NEO4J_URI = os.environ.get("NEO4J_URI")
NEO4J_BENUTZER = os.environ.get("NEO4J_USERNAME", "neo4j") # 'neo4j' als Standard
NEO4J_PASSWORT = os.environ.get("NEO4J_PASSWORD")

# Der Test-Funktionsname MUSS mit 'test_' beginnen
def test_neo4j_connection():
    """
Prüft, ob die Verbindung zur Neo4j Aura DB hergestellt werden kann.
    """
    
    # 1. Vorbedingung: Prüfen, ob die Secrets (Schlüssel) überhaupt da sind
    # 'assert' ist das Schlüsselwort in PyTest. 
    # Wenn die Aussage dahinter FALSCH ist, bricht der Test hier ab.
    assert NEO4J_URI is not None, "Fehler: NEO4J_URI ist nicht gesetzt!"
    assert NEO4J_PASSWORT is not None, "Fehler: NEO4J_PASSWORD ist nicht gesetzt!"

    driver = None
    try:
        # 2. Aktion: Versuche, die Verbindung herzustellen
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_BENUTZER, NEO4J_PASSWORT))
        
        # 3. Prüfung: Der Befehl .verify_connectivity() 
        # wirft einen Fehler, wenn es fehlschlägt.
        driver.verify_connectivity()
        
        # Wenn wir hier ankommen, ist alles gut gelaufen.
        # Wir können das explizit mit 'assert True' festhalten.
        assert True 

    except Exception as e:
        # 4. Fehlerfall: Wenn ein Fehler auftritt, lassen wir den Test fehlschlagen
        # und geben den Fehler aus.
        assert False, f"Verbindungsfehler zur DB aufgetreten: {e}"
        
    finally:
        # 5. Aufräumen: Immer die Verbindung schließen
        if driver:
            driver.close()