# 💡 Local RAG Chatbot for Inforiver Blog Content

A fully local Retrieval-Augmented Generation (RAG) chatbot powered by **Mistral**, **FAISS**, and **Streamlit** — trained on Inforiver blog content. No OpenAI, no tokens, no cloud dependencies.

---

## 📌 Features

- 💬 Ask natural language questions about Power BI, scheduling, writeback, and more
- 🔍 Retrieves relevant blog chunks using **FAISS** and semantic search
- 🧠 Generates grounded answers using **Mistral 7B** via **Ollama**
- 📚 Built with **local blog content (Excel)** from Inforiver
- 💻 Runs completely offline — perfect for secure or internal use cases

---

## 🛠️ Tech Stack

- [Mistral 7B](https://ollama.com/library/mistral) via [Ollama](https://ollama.com)
- [FAISS](https://github.com/facebookresearch/faiss) for vector search
- [SentenceTransformers](https://www.sbert.net/) for generating embeddings
- [Streamlit](https://streamlit.io) for building the chatbot UI
- Blog content chunked and loaded from Excel files

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/local-rag-chatbot-inforiver.git
cd local-rag-chatbot-inforiver
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run Ollama & Pull Mistral
```bash
ollama run mistral
```
Keep this running in the background.

### 4. Prepare Your Blog Data
Place your Excel blog files (like `PowerBI_Report_Delivery_Chunks.xlsx`, etc.) into the project root. Modify the script to load more if needed.

### 5. Embed & Index the Content
```bash
python generate_faiss_index.py
```

### 6. Run the Chatbot
```bash
streamlit run rag_chatbot_app.py
```

---

## 🧠 How It Works
1. User question is embedded
2. FAISS finds top-k similar blog chunks
3. Chunks + question are passed as a prompt to Mistral
4. Mistral generates a grounded response using local context

---

## 📚 Source Content
Blog content used in this project comes from **Inforiver's official website**:  
➡️ https://inforiver.com

Topics include:
- Power BI report scheduling
- Writeback matrix features
- Report bursting and delivery

---

## 🛡️ Why Local?
- 🔐 Full data privacy
- 💸 Zero API cost
- 🧩 Easy to adapt to any internal docs or domain-specific knowledge

---

## 📦 To-Do / Roadmap
- [ ] Upload support for PDF/Docs
- [ ] Source link highlighting
- [ ] Feedback thumbs up/down
- [ ] Hybrid search + reranking
- [ ] Docker setup for easy deployment

---

## 📣 Contributions
Feel free to fork this project, suggest improvements, or use it to build your own chatbot trained on internal or private data.

---

## 📄 License
MIT License
