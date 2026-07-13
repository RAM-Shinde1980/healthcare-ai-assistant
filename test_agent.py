from app.agent import HealthcareAgent

agent = HealthcareAgent()

question = "What is diabetes?"

answer = agent.ask(question)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(answer)