from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from src.config import GROQ_API_KEY

DB_PATH = "vectorstore"


def get_rag_chain():
    # 1. Load the Vector Database with the local embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)

    # 2. Create Retriever
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # 3. Initialize the LLM using Groq (FREE & EXTREMELY FAST)
    # If 'GPT OSS 20B' isn't a valid string, try 'llama-3.1-8b-instant'
    # (Groq's standard fast model). Check their Docs for the exact string.
    llm = ChatGroq(
        temperature=0.1,
        groq_api_key=GROQ_API_KEY,
        model_name="openai/gpt-oss-20b",  # Updated to the current, active model
    )

    # 4. Create the Prompt Template
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer the question. "
        "If you don't know the answer, say that you don't know. "
        "Use three sentences maximum and keep the answer concise.\n\n"
        "Context: {context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    # 5. Build the Chain
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    return rag_chain
