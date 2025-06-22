import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# 1. Load blog data
df1 = pd.read_excel("PowerBI_Report_Delivery_Chunks.xlsx")
df = pd.concat([df1], ignore_index=True)

# 2. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 3. Generate embeddings
embeddings = model.encode(df['content'].tolist(), show_progress_bar=True)

# 4. Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings).astype('float32'))

# 5. Save files locally
faiss.write_index(index, "blog_chunks_faiss.index")
df.to_csv("blog_chunks_metadata.csv", index=False)

print("✅ Embeddings saved to FAISS, metadata saved as CSV.")
