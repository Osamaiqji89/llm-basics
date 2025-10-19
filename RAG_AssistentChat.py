import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# --- VORBEREITUNG (Stelle sicher, dass der API-Schlüssel gesetzt ist) --- Yt_ImeHYLeioFtnOV0xodtEacujSl6RMueR__pgYr4E neo4j
if "GROQ_API_KEY" not in os.environ:
    print("Fehler: GROQ_API_KEY nicht gefunden.")
    print("Bitte setze die Umgebungsvariable, z.B.:")
    print("export GROQ_API_KEY='dein-schluessel-hier'")
    exit()

# --- 1. SETUP (Modelle und DB laden) ---
print("Lade Embedding-Modell...")
embedding_model = HuggingFaceEmbeddings(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

print("Lade Vektor-Datenbank aus './chroma_db'...")
vector_store = Chroma(
    persist_directory="./chroma_db", 
    embedding_function=embedding_model
)

# 1a. Der Retriever (Sucht die Chunks) 🔍
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# 1b. Das Chat-Modell (Schreibt die Antwort) ✍️
llm = ChatGroq(model_name="llama-3.1-8b-instant")

# 1c. Die Prompt-Schablone (Die Anweisung) 📝
rag_prompt = ChatPromptTemplate.from_template(
    """Du bist ein technischer Assistent. Beantworte die folgende Frage präzise, 
basierend auf dem folgenden Kontext:

{context}

Frage: {question}
"""
)

# 1d. Der Output Parser (Macht die Antwort zu reinem Text)
output_parser = StrOutputParser()


# --- 2. DIE RAG-KETTE (PIPELINE) BAUEN --- 🔗
# Hier passiert die Magie. Wir nutzen den Pipe-Operator '|'

# Zuerst definieren wir, wie 'context' und 'question' gefüllt werden:
setup_and_retrieval = RunnableParallel(
    # Der Retriever holt den Kontext basierend auf der Frage
    context=retriever, 
    # Die Frage wird einfach durchgereicht
    question=RunnablePassthrough() 
)

# Jetzt die komplette Kette:
# 1. 'setup_and_retrieval' holt die Daten
# 2. 'rag_prompt' füllt die Schablone aus
# 3. 'llm' generiert die Antwort
# 4. 'output_parser' extrahiert den Text
chain = setup_and_retrieval | rag_prompt | llm | output_parser

print("\n--- Technical Document Assistant ist BEREIT ---")
print("Stelle eine Frage zu deinem Dokument (z.B. 'Was ist das Automation Interface?'):")


# --- 3. CHAT-SCHLEIFE ---
try:
    while True:
        frage = input("\nDEINE FRAGE: ")
        if frage.lower() in ["exit", "quit", "ende"]:
            break
        
        # Die Kette aufrufen und die Antwort streamen (Wort für Wort)
        print("\nKI-ANTWORT: ", end="", flush=True)
        for chunk in chain.stream(frage):
            print(chunk, end="", flush=True)
        print()

except KeyboardInterrupt:
    print("\nAuf Wiedersehen!")