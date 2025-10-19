# ==================================================================
#  TEIL 1: UNSERE PROMPT-SCHABLONEN
# ==================================================================

# 📜 System-Prompt (Rolle) für die Zusammenfassung
# (Genau der, den wir gerade entwickelt haben)
SYSTEM_PROMPT_SUMMARY = """
Du bist ein hilfreicher Autor, dessen einzige Aufgabe es ist, 
jeden Text, der dir gegeben wird, in genau einem Satz zusammenzufassen.
"""

# 📜 System-Prompt für Code-Review
# (Den schauen wir uns als Nächstes an)
SYSTEM_PROMPT_CODE_REVIEW = """
Du bist ein erfahrener Software-Entwickler. 
Deine Aufgabe ist es, Code-Snippets zu prüfen und 
drei konkrete Verbesserungsvorschläge in einer Liste zu machen.
"""
# 📜 System-Prompt für SQL-Analyse
SYSTEM_PROMPT_SQL_REVIEW = """
Du bist ein Datenbank-Experte 📊. Deine Aufgabe ist es, jeden SQL-Code, 
der dir gegeben wird, sorgfältig zu analysieren und 
auf Fehler oder ineffiziente Abfragen zu prüfen.
"""
# ==================================================================
#  TEIL 2: DIE "KI" (Simulation)
# ==================================================================
# Diese Funktion simuliert das Senden an eine KI.
# Sie baut den finalen Prompt zusammen und druckt ihn aus.
def simuliere_ki_anfrage(system_prompt, user_prompt):
    """Baut den finalen Prompt zusammen und simuliert den Sende-Vorgang."""
    
    # Hier werden Rolle und Aufgabe kombiniert
    finaler_prompt = f"""
===================================================
[START SYSTEM PROMPT]
{system_prompt}
[END SYSTEM PROMPT]
===================================================

[START USER PROMPT]
{user_prompt}
[END USER PROMPT]
===================================================
"""
    
    print("--- Sende folgende Anfrage an die KI: ---")
    print(finaler_prompt)
    print("-------------------------------------------\n")

# ==================================================================
#  TEIL 3: PIPELINE AUSFÜHREN (Zusammenfassung)
# ==================================================================

# 🗣️ User-Prompt (Aufgabe 1: Zusammenfassung)
text_zum_zusammenfassen = """
Künstliche Intelligenz (KI) ist ein Teilgebiet der Informatik, 
das sich mit der Schaffung von Maschinen befasst, die Aufgaben 
ausführen können, die typischerweise menschliche Intelligenz erfordern. 
Dazu gehören Lernen, Problemlösung und Spracherkennung.
"""

# Wir rufen unsere Pipeline auf:
simuliere_ki_anfrage(SYSTEM_PROMPT_SUMMARY, text_zum_zusammenfassen)

# ==================================================================
#  TEIL 4: PIPELINE AUSFÜHREN (Code-Review)
# ==================================================================

# 🗣️ User-Prompt (Aufgabe 2: Code-Review)
code_zum_pruefen = """
def add(a, b):
    result = a + b
    return result
"""

# Wir rufen unsere Pipeline mit der *anderen* Rolle auf:
simuliere_ki_anfrage(SYSTEM_PROMPT_CODE_REVIEW, code_zum_pruefen)

# ==================================================================
#  TEIL 5: PIPELINE AUSFÜHREN (SQL-Analyse)
# ==================================================================

# 🗣️ User-Prompt (Aufgabe 3: SQL-Analyse)
sql_zum_pruefen = "SELECT * FROM User WHERE UserId = 10;"

# Wir rufen unsere Pipeline mit der SQL-Rolle auf:
simuliere_ki_anfrage(SYSTEM_PROMPT_SQL_REVIEW, sql_zum_pruefen)