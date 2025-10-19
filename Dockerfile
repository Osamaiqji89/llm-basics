# 1. Start: Nimm eine offizielle Basis-Box (ein Mini-Linux mit Python 3.10)
FROM python:3.10-slim

# 2. Setze den Ordner in der Box, in dem wir arbeiten wollen
WORKDIR /app

# 3. Kopiere ZUERST die Zutatenliste (requirements.txt) in die Box
# (Das ist ein Trick, damit Docker schnelle baut)
COPY requirements.txt .

# 4. Installiere die Zutaten (Bibliotheken) in der Box
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kopiere jetzt unseren restlichen Code (das "Rezept") in die Box
COPY GraphAssistent.py .

# 6. Das ist der Befehl, der ausgeführt wird, wenn die Box "gestartet" wird
CMD ["python", "GraphAssistent.py"]