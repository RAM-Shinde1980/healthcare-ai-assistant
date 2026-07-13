from app.embeddings import EmbeddingManager

manager = EmbeddingManager()

db = manager.load_vector_store()

print("✅ Vector Database Loaded Successfully!")
print(f"Total vectors: {db._collection.count()}")