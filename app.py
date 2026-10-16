import streamlit as st
from src.rag_pipeline import get_rag_chain

st.set_page_config(page_title="Advanced RAG Chatbot", layout="centered")
st.title("📄 Chat with your PDF (100% Free & Local)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Load the RAG chain (cached so it doesn't reload every time)
@st.cache_resource
def load_chain():
    return get_rag_chain()


try:
    rag_chain = load_chain()
except Exception as e:
    st.error(f"Error loading database. Did you run ingest.py first? Error: {e}")
    st.stop()

# React to user input
if prompt := st.chat_input("Ask a question about your PDF..."):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get AI response
    with st.chat_message("assistant"):
        # Use stream instead of invoke
        stream = rag_chain.stream({"input": prompt})

        # Create a generator to extract just the answer text
        def stream_generator():
            for chunk in stream:
                if "answer" in chunk:
                    yield chunk["answer"]

        # st.write_stream displays the text as it arrives
        answer = st.write_stream(stream_generator())

    st.session_state.messages.append({"role": "assistant", "content": answer})
