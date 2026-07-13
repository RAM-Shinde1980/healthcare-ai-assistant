from app.xml_loader import load_all_documents

documents = load_all_documents()

print(f"Documents Loaded: {len(documents)}")

if documents:
    print("\nFirst Document:\n")
    print(documents[0].page_content)

    print("\nMetadata:\n")
    print(documents[0].metadata)
else:
    print("No documents were loaded.")