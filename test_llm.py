from app.rag import RAGRetriever
from app.llm import LLMManager

question = "What is diabetes?"

rag = RAGRetriever()
documents = rag.retrieve(question)

llm = LLMManager()

answer = llm.generate_answer(question, documents)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(answer)