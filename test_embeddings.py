from app.xml_loader import load_all_documents
from app.embeddings import EmbeddingManager

documents = load_all_documents()

manager = EmbeddingManager()

db = manager.create_vector_store(documents)

print("Vector Store Created Successfully!")
print(f"Total vectors: {db._collection.count()}")