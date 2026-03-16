from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os


def create_vector_store():

    # Load knowledge base
    with open("data/career_knowledge.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # Split text into chunks
    splitter = CharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    documents = splitter.split_text(text)

    # Load local embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # Create FAISS vector database
    vector_db = FAISS.from_texts(documents, embeddings)

    # Save vector database locally
    os.makedirs("vector_db", exist_ok=True)
    vector_db.save_local("vector_db")

    print("\nVector database created successfully!")
    print("Saved inside folder: vector_db")


if __name__ == "__main__":
    create_vector_store()