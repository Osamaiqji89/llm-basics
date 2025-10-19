from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
# NEU: Wir brauchen jetzt ein Chat-Modell für die "Generation"
# Wir installieren es mit: pip install langchain_groq
# (Du musst dir einen kostenlosen API-Key auf groq.com holen
# und ihn als Umgebungsvariable 'GROQ_API_KEY' setzen)
# ----
# HINWEIS: Da ich nicht auf deine Umgebungsvariablen zugreifen kann,
# simuliere ich den letzten Schritt (Generation) im Code unten.
# ----

# --- SETUP (Laden der fertigen Datenbank) ---

print("Lade Embedding-Modell...")
embedding_model = HuggingFaceEmbeddings(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

print("Lade Vektor-Datenbank aus './chroma_db'...")
vector_store = Chroma(
    persist_directory="./chroma_db", 
    embedding_function=embedding_model
)

# 1. RETRIEVAL (Abrufen) 🔍
# Wir erstellen einen "Retriever", der die Suche übernimmt
retriever = vector_store.as_retriever(
    search_kwargs={"k": 3} # "k: 3" bedeutet: "Gib mir die 3 besten Treffer" 
)

# --- FRAGE STELLEN ---

deine_frage = "Was ist das Automation Interface?"

print(f"\nSuche nach relevanten Chunks für die Frage: '{deine_frage}'")

# Das Retrieval passiert hier:
relevante_chunks = retriever.invoke(deine_frage)

print(f"\n--- {len(relevante_chunks)} relevante Chunks gefunden: ---")
for i, chunk in enumerate(relevante_chunks):
    print(f"\n[CHUNK {i+1}]:")
    print(chunk.page_content)
    print(f"(Quelle: Seite {chunk.metadata.get('page', '?')})")


# 2. GENERATION (Erzeugen) ✍️
# HIER würden wir die `relevante_chunks` + `deine_frage` 
# an ein Chat-Modell (wie Groq, OpenAI oder ein lokales Modell) senden.

# --- Simulation der Generation ---
print("\n\n--- [Simulierte KI-Antwort] ---")
print(f"Basierend auf den gefundenen Dokumenten (z.B. Chunk 1 von Seite {relevante_chunks[0].metadata.get('page', '?')}),")
print("-------------------------------")