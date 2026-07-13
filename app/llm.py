from langchain_ollama import ChatOllama

from app.config import Config
from app.logger import logger
from app.prompts import build_prompt


class LLMManager:
    """
    Handles communication with the Ollama LLM.
    """

    def __init__(self):
        logger.info(f"Loading LLM: {Config.MODEL_NAME}")

        self.llm = ChatOllama(
            model=Config.MODEL_NAME,
            temperature=0,
        )

    def generate_answer(self, question: str, documents: list):
        """
        Generate an answer using the retrieved documents.
        """

        context = "\n\n".join(
            [doc.page_content for doc in documents]
        )

        prompt = build_prompt(
            context=context,
            question=question
        )

        logger.info("Generating response from LLM...")

        response = self.llm.invoke(prompt)

        return response.content