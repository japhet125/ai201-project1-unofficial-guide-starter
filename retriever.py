import chromadb
from chromadb.utils import embedding_functions

from ingest import build_chunks

CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "cuny_reviews"

# Embedding model
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# ChromaDB client
client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_function,
    metadata={"hnsw:space": "cosine"}
)


def ingest_to_chroma():
    """
    Load chunks from ingest.py and store them in ChromaDB.
    """
    chunks = build_chunks()

    if collection.count() > 0:
        print(f"Collection already contains {collection.count()} chunks.")
        return

    collection.add(
        ids=[chunk["id"] for chunk in chunks],
        documents=[chunk["text"] for chunk in chunks],
        metadatas=[
            {
                "source": chunk["source"],
                "chunk_number": chunk["chunk_number"]
            }
            for chunk in chunks
        ]
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB.")


def retrieve(query, n_results=5):
    """
    Retrieve the most relevant chunks for a query.
    """

    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    retrieved = []

    for i in range(len(documents)):
        retrieved.append({
            "text": documents[i],
            "source": metadatas[i]["source"],
            "distance": distances[i]
        })

    return retrieved


if __name__ == "__main__":
    ingest_to_chroma()

    query = input("Ask a question: ")

    results = retrieve(query)

    print("\nTop Results:\n")

    for result in results:
        print("=" * 60)
        print(f"Source: {result['source']}")
        print(f"Distance: {result['distance']:.4f}")
        print(result["text"])
        print()