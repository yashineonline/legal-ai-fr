   # build_faiss_index.py
   import numpy as np
   import faiss
   from sentence_transformers import SentenceTransformer

   # Example: Embed legal clauses and save to FAISS
   clauses = ["Clause 1 text...", "Clause 2 text..."]  # Replace with your legal corpus
   model = SentenceTransformer("dangvantuan/sentence-camembert-base")
   embeddings = model.encode(clauses)

   index = faiss.IndexFlatL2(embeddings.shape[1])
   index.add(embeddings)
   faiss.write_index(index, "faiss_index.bin")