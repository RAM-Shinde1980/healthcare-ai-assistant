import os
import xml.etree.ElementTree as ET

from langchain_core.documents import Document

from app.config import Config
from app.logger import logger


def load_single_xml(file_path: str):
    """
    Parse one MedQuAD XML file and return a list of LangChain Documents.
    """

    documents = []

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        focus = root.findtext("Focus", default="Unknown")
        source = root.attrib.get("source", "Unknown")
        url = root.attrib.get("url", "")

        qapairs = root.find("QAPairs")

        if qapairs is None:
            return documents

        for qa in qapairs.findall("QAPair"):

            question = qa.findtext("Question", default="")
            answer = qa.findtext("Answer", default="")

            content = f"""
Topic:
{focus}

Question:
{question}

Answer:
{answer}
"""

            doc = Document(
                page_content=content.strip(),
                metadata={
                    "focus": focus,
                    "source": source,
                    "url": url,
                    "file_name": os.path.basename(file_path),
                },
            )

            documents.append(doc)

    except Exception as e:
        logger.error(f"Failed to parse {file_path}: {e}")

    return documents


def load_all_documents():
    """
    Load every XML file from the data folder.
    """

    logger.info("Loading XML documents...")

    all_documents = []

    for root_dir, _, files in os.walk(Config.DATA_FOLDER):

        for file in files:

            if file.endswith(".xml"):

                path = os.path.join(root_dir, file)

                docs = load_single_xml(path)

                all_documents.extend(docs)

    logger.info(f"Loaded {len(all_documents)} documents.")

    return all_documents