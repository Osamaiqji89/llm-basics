from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings 
from langchain_community.vectorstores import Chroma 

# 1. LADEN (Load)
pdf_pfad = "Workflow-Automation.pdf"
loader = PyPDFLoader(pdf_pfad)

# Die 'load'-Methode liest das PDF ein
dokumente = loader.load()

# Lass uns prüfen, was wir geladen haben:
print(f"'{pdf_pfad}' geladen.")
print(f"Das PDF hat {len(dokumente)} Seiten (Dokumente).")
print("\n--- Beispiel-Inhalt (Seite 1): ---")
print(dokumente[0].page_content[:120] + "...") 

# 2. SPLITTEN (Chunking)
# Wir definieren, wie groß unsere "Häppchen" sein sollen.
# chunk_size = Wie viele Zeichen pro Häppchen?
# chunk_overlap = Wie viele Zeichen sollen sich überlappen?
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=200
)

# Wir zerlegen die geladenen Seiten in kleinere Chunks
chunks = text_splitter.split_documents(dokumente)

print(f"Die {len(dokumente)} Seiten wurden in {len(chunks)} Chunks zerlegt.")
print("\n--- Beispiel-Chunk: ---")
print(chunks[0].page_content)

# 3. EMBEDDEN & 4. SPEICHERN (Embed & Store)
# Wir definieren, welches Embedding-Modell wir nutzen wollen
embedding_model = HuggingFaceEmbeddings(
    model_name="paraphrase-multilingual-MiniLM-L12-v2"
)

# Wir erstellen die Vektor-Datenbank (ChromaDB) direkt aus den Chunks.
# Dieser Befehl macht beides:
# a) Erstellt die Embeddings (Zahlen-Vektoren) für jeden Chunk
# b) Speichert sie im Vector Store (Chroma)
print("Starte Indexierung (Embedden & Speichern)...")
vector_store = Chroma.from_documents(
    documents=chunks, 
    embedding=embedding_model,
    persist_directory="./chroma_db" # Ein Ordner, um die DB zu speichern
)

print(f"Indexierung abgeschlossen! Vektor-Datenbank in './chroma_db' gespeichert.")