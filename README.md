# LLM-Lernen-Grundlage

Ein Lernprojekt zur Integration von Large Language Models (LLM) mit Neo4j-Graphdatenbanken und LangChain. Ziel ist es, KI-gestützte Abfragen auf Graphdaten zu ermöglichen und die Grundlagen von LLM-Anwendungen praktisch zu erlernen.

## Features
- Verbindung zu einer Neo4j Aura Datenbank
- Nutzung von LangChain und Groq LLMs
- Automatisierte Cypher-Abfragen und KI-Antworten
- Docker- und pytest-Unterstützung

## Installation

1. **Python-Umgebung vorbereiten**
   ```bash
   pip install -r requirements.txt
   ```
2. **Umgebungsvariablen setzen** (z.B. in PowerShell):
   ```powershell
   $env:GROQ_API_KEY="<dein_groq_api_key>"
   $env:NEO4J_URI="neo4j+s://<deine_neo4j_uri>"
   $env:NEO4J_USERNAME="neo4j"
   $env:NEO4J_PASSWORD="<dein_neo4j_passwort>"
   ```
3. **Starten**
   ```bash
   python GraphAssistent.py
   ```

## Dateien und Beschreibung

| Datei                              | Beschreibung                                                                 |
|------------------------------------|------------------------------------------------------------------------------|
| GraphAssistent.py                  | Hauptskript: Verbindet LLM (Groq) mit Neo4j, stellt Fragen und zeigt Antworten. |
| agent.py                           | (Vermutlich) Logik für Agenten oder KI-Interaktion.                          |
| prompt_pipeline.py                 | Pipeline zur Verarbeitung von Prompts und KI-Dialogen.                       |
| ragAssistentChat.py                | Chat-Interface für Retrieval-Augmented Generation (RAG) mit Assistenten.      |
| ragAssistentData.py                | Datenverwaltung und -aufbereitung für RAG-Workflows.                         |
| ragAssistentGraphBuild.py          | Aufbau und Verwaltung von Graphstrukturen für RAG und KI.                     |
| ragAssistentGraphConnTest.py       | Testet die Verbindung und Funktionalität des Graphen (z.B. Neo4j).           |
| Simulierte_AI_Antwort.py           | Simulation von KI-Antworten, z.B. für Tests oder Demo-Zwecke.                |
| test_graph.py                      | Pytest-Test: Prüft die Verbindung zur Neo4j-Datenbank.                       |
| requirements.txt                   | Listet alle benötigten Python-Pakete mit Versionen.                          |
| Dockerfile                         | Docker-Konfiguration für das Projekt.                                        |
| .gitignore                         | Ignoriert temporäre, sensible und Build-Dateien für Git.                     |
| chroma_db/                         | Ordner für lokale Datenbank- oder Vektorspeicherdateien.                     |
| Neo4j-*-Created-*.txt              | Export- oder Logdateien von Neo4j Aura.                                      |
| test.txt                           | Beispiel- oder Testdatei (Inhalt variabel).                                  |

## Nutzung mit Docker

```bash
docker build -t llm-lernen-grundlage .
docker run -e GROQ_API_KEY=<dein_groq_api_key> -e NEO4J_URI=<deine_neo4j_uri> -e NEO4J_USERNAME=neo4j -e NEO4J_PASSWORD=<dein_neo4j_passwort> llm-lernen-grundlage
```

## Hinweise
- Die Umgebungsvariablen sind für den Betrieb zwingend erforderlich.
- Die Neo4j-Zugangsdaten sollten niemals öffentlich geteilt werden.
- Für eigene Experimente können die Skripte beliebig angepasst werden.

---

**Dieses Projekt dient ausschließlich Lern- und Experimentierzwecken!**