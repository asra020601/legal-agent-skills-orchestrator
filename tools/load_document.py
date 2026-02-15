from pathlib import Path
import os
from langchain.tools import tool
from docx import Document

DATA_DIR = Path(os.getenv("DATA_DIR"))

@tool
def load_document(document_name: str) -> str:
    """
    Load a document from the data folder by name (without extension).
    """
    path = DATA_DIR / f"{document_name}.docx"

    if not path.exists():
        return f"Document '{document_name}' not found in data folder."

    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)