from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from services.embedding_service import get_embedding_model
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

DATA_FOLDER = "data"
VECTOR_DB_PATH = "vectorstore/index"

def build_index():

    documents = []

    for file in os.listdir(DATA_FOLDER):
        if file.endswith(".txt"):
            file_path = os.path.join(DATA_FOLDER, file)
            loader = TextLoader(file_path, encoding="utf-8")
            documents.extend(loader.load())

    if not documents:
        print("❌ No documents found in data folder.")
        return

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    embeddings = get_embedding_model()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    vectorstore.persist()

    print("✅ Vector DB created successfully!")


if __name__ == "__main__":
    build_index()