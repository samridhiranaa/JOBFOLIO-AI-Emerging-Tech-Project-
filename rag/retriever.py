from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def retrieve_context(query, k=2):

    # Load the same embedding model used for indexing
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # Load the FAISS vector database
    vector_db = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Perform similarity search
    docs = vector_db.similarity_search(query, k=k)

    results = []

    for doc in docs:
        results.append(doc.page_content)

    return results


if __name__ == "__main__":

    query = "Docker projects"

    results = retrieve_context(query)

    print("\nRecommended Context:\n")

    for i, r in enumerate(results, 1):
        print(f"{i}. {r}\n")