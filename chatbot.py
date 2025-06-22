import streamlit as st
import faiss
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import requests

# Load FAISS index + metadata
index = faiss.read_index("blog_chunks_faiss.index")
metadata = pd.read_csv("blog_chunks_metadata.csv")

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# 🔄 Query embedding
def get_query_embedding(query):
    return embed_model.encode([query])[0]

# 🔍 Retrieve top K chunks
def retrieve_chunks(query_embedding, k=3):
    query_vector = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(query_vector, k)
    return metadata.iloc[indices[0]]

# 🧠 Build prompt for LLM
def build_prompt(chunks, question):
    context = "\n\n".join(chunks["content"].tolist())
    prompt = f"""You are a helpful assistant specialized in Power BI and Inforiver.

Use the following blog content to answer the user's question.

Context:
{context}

Question: {question}

Answer:"""
    return prompt

# 💬 Call local Mistral via Ollama API
def call_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

# 🖼️ Streamlit UI
st.title("💡 Local RAG Chatbot (Mistral + FAISS)")

user_query = st.text_input("Ask your question:")

if user_query:
    with st.spinner("Thinking..."):
        q_embed = get_query_embedding(user_query)
        top_chunks = retrieve_chunks(q_embed, k=3)
        prompt = build_prompt(top_chunks, user_query)
        answer = call_llm(prompt)

    st.markdown("### 💬 Answer")
    st.write(answer)

    st.markdown("### 📚 Sources")
    for i, row in top_chunks.iterrows():
        st.info(f"**{row['title']}**\n\n{row['content'][:300]}...")
