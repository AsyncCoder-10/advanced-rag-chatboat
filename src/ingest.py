import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

DATA_PATH = "data"
DB_PATH = "vectorstore"


def ingest_documents():
    print("--- Starting Ingestion ---")

    # 1. Load Documents
    documents = []
    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            print(f"Loading {file}...")
            loader = PyPDFLoader(os.path.join(DATA_PATH, file))
            documents.extend(loader.load())

    if not documents:
        print("No PDFs found in the data/ folder. Please add a PDF.")
        return

    # 2. Chunk Documents
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks.")

    # 3. Embed and Store using a free, local model
    print("Loading embedding model and saving to vector database...")
    # This model runs locally on your CPU, no API key needed.
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks, embedding=embeddings, persist_directory=DB_PATH
    )
    vectorstore.persist()
    print("--- Ingestion Complete! ---")


if __name__ == "__main__":
    ingest_documents()
