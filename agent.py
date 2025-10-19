import json

# ==================================================================
#  TEIL 1: DAS WERKZEUG (TOOL) 🧰
# ==================================================================
# Das ist unser Tool. Es nimmt einen Dateinamen, liest die Datei
# und gibt ein *Ergebnis* als einfaches Python-Dictionary zurück.
def analyze_file_content(filename):
    """Liest eine Datei und zählt die Wörter darin."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            word_count = len(content.split())
            
            # Das Tool gibt ein strukturiertes Ergebnis zurück
            return {
                "status": "success",
                "filename_analyzed": filename,
                "word_count": word_count,
                "char_count": len(content)
            }
    except FileNotFoundError:
        return {
            "status": "error",
            "message": f"Datei '{filename}' nicht gefunden."
        }

# ==================================================================
#  TEIL 2: DER "AGENT" (simuliert) 🤖
# ==================================================================
# Diese Funktion simuliert unseren Agenten.
def run_agent_task(user_request):
    
    print(f"--- Neues Ziel vom User: '{user_request}' ---")
    
    # 1. PLANUNG (Reasoning)
    # Der Agent "versteht" die Anfrage und entscheidet,
    # 'analyze_file_content' mit dem Argument 'test.txt' aufzurufen.
    print("\n[Agent 🤖 denkt]: OK, ich muss das Dateianalyse-Tool für 'test.txt' nutzen.")
    
    # 2. KOMMUNIKATION (MCP: Agent -> Tool)
    # Der Agent formatiert seinen Plan als JSON-Nachricht (Tool Call).
    mcp_tool_call = {
        "tool_call": {
            "name": "analyze_file_content",
            "arguments": {
                "filename": "test.txt"
            }
        }
    }
    
    # Wir drucken das JSON aus, um es zu sehen:
    print("\n[Agent 🤖 sendet MCP-Nachricht an Tool]:")
    print(json.dumps(mcp_tool_call, indent=2))
    
    # 3. TOOL-AUSFÜHRUNG
    # In echt würde das MCP-Protokoll das Tool "remote" aufrufen.
    # Wir rufen hier einfach direkt die Python-Funktion auf.
    tool_name = mcp_tool_call["tool_call"]["name"]
    tool_args = mcp_tool_call["tool_call"]["arguments"]
    
    if tool_name == "analyze_file_content":
        # Hier rufen wir unser echtes Python-Tool auf:
        result_data = analyze_file_content(tool_args["filename"])
    
    # 4. KOMMUNIKATION (MCP: Tool -> Agent)
    # Das Tool schickt sein Ergebnis als JSON-Nachricht zurück.
    mcp_tool_result = {
        "tool_result": {
            "name": "analyze_file_content",
            "content": result_data  # Hier ist das Ergebnis-Dictionary von oben
        }
    }
    
    print("\n[Tool 🧰 sendet MCP-Antwort an Agent]:")
    print(json.dumps(mcp_tool_result, indent=2))
    
    # 5. SYNTHESE
    # Der Agent nimmt das "content"-Feld aus dem Ergebnis...
    final_result = mcp_tool_result["tool_result"]["content"]
    
    # ...und formuliert eine nette Antwort für den Menschen.
    if final_result["status"] == "success":
        antwort = (
            f"Analyse fertig: Die Datei '{final_result['filename_analyzed']}' "
            f"hat {final_result['word_count']} Wörter."
        )
    else:
        antwort = f"Fehler bei der Analyse: {final_result['message']}"

    print("\n[Agent 🤖 antwortet dem User]:")
    print(antwort)
    print("-------------------------------------------------")


# ==================================================================
#  PROJEKT STARTEN
# ==================================================================
# Wir tun so, als würde ein User die Anfrage stellen:
run_agent_task("Bitte analysiere die Datei test.txt für mich.")