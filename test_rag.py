from app.rag import RAGRetriever

rag = RAGRetriever()

documents = rag.retrieve("What is diabetes?")

print(f"Retrieved {len(documents)} documents\n")

for i, doc in enumerate(documents, start=1):
    print("=" * 60)
    print(f"Document {i}")
    print("=" * 60)
    print(doc.page_content[:500])
    print()
    print(doc.metadata)
    print()