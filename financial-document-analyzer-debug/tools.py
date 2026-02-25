from langchain_community.document_loaders import PyPDFLoader


def read_financial_document(path: str) -> str:
    """
    Reads a financial PDF file and returns combined cleaned text.
    """
    loader = PyPDFLoader(path)
    documents = loader.load()

    full_text = ""
    for doc in documents:
        full_text += doc.page_content.strip() + "\n"

    return full_text