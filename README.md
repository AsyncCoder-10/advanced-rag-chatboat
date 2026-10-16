# 📄 Advanced RAG Chatbot: Chat with your PDF

A fully functional, high-speed Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content. 

This project was built to demonstrate a production-ready RAG architecture, moving beyond basic scripts to a modular, decoupled system that balances cost, speed, and accuracy.

## ✨ Features

- **100% Free Embeddings:** Uses Hugging Face `sentence-transformers` locally, meaning you don't pay for embedding API calls.
- **Ultra-Fast LLM Inference:** Integrates with **Groq API** to run open-source LLMs on specialized LPU hardware, delivering near-instant responses.
- **Advanced Chunking:** Uses `RecursiveCharacterTextSplitter` with overlapping chunks to prevent context loss at document boundaries.
- **Vector Search:** Utilizes **ChromaDB** for efficient local vector storage and similarity search.
- **Real-time Streaming:** The Streamlit UI streams the LLM's response word-by-word, providing a ChatGPT-like user experience.
- **Decoupled Architecture:** Clean separation of concerns (Ingestion, RAG Pipeline, UI, Configuration).

## 🏗️ Architecture

The system is divided into an offline Ingestion Phase and an online Inference Phase.

```mermaid
graph TD
    subgraph Ingestion Phase [Offline]
        A[PDF Documents] --> B[PyPDFLoader]
        B --> C[RecursiveCharacterTextSplitter]
        C --> D[HuggingFace Embeddings]
        D --> E[(ChromaDB Vector Store)]
    end

    subgraph Inference Phase [Online]
        F[User Query] --> G[Streamlit UI]
        G --> H[Retriever]
        E --> H
        H --> I[Groq LLM API]
        I --> J[Streaming Response]
        J --> G
    end
🛠️ Tech Stack
Framework: LangChain (langchain, langchain-classic, langchain-community)

LLM Inference: Groq API (langchain-groq) - Model: openai/gpt-oss-20b

Embeddings: Hugging Face (sentence-transformers/all-MiniLM-L6-v2)

Vector Database: ChromaDB

Frontend: Streamlit

Document Loading: PyPDF

📁 Project Structure
text
advanced-rag-chatbot/
│
├── .env                  # Stores your Groq API key (not committed to Git)
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
│
├── data/                 # Place your PDF files here
│   └── your_document.pdf
│
├── vectorstore/          # ChromaDB saves its database here (auto-generated)
│
├── src/                  # Core source code
│   ├── __init__.py
│   ├── config.py         # Loads environment variables
│   ├── ingest.py         # Script to process PDFs and build the vector DB
│   └── rag_pipeline.py   # Core logic for retrieval, prompting, and generation
│
└── app.py                # Streamlit web interface
🚀 Getting Started
Follow these steps to set up and run the project locally.

1. Clone the Repository
bash
git clone https://github.com/your-username/advanced-rag-chatbot.git
cd advanced-rag-chatbot
2. Set Up Virtual Environment
bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
3. Install Dependencies
bash
pip install -r requirements.txt
4. Set Up Environment Variables
Create a .env file in the root directory and add your Groq API key. You can get a free API key from console.groq.com.

text
GROQ_API_KEY=gsk_your_actual_api_key_here
5. Add Your Documents
Place the PDF file(s) you want to chat with inside the data/ folder.

🏃‍♂️ How to Run
Step 1: Ingest the Documents
Run the ingestion script to process your PDFs, create embeddings, and store them in ChromaDB.

bash
python -m src.ingest
You should see a success message and a new vectorstore/ folder will be created.

Step 2: Run the Application
Start the Streamlit web app.

bash
streamlit run app.py
The app will open in your browser at http://localhost:8501

Working Video


https://github.com/user-attachments/assets/62c20db7-e796-4810-93cb-ce24ae8c606d




