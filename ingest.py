from pathlib import Path
import re

DOCUMENTS_DIR = Path("documents")
CHUNK_SIZE = 500
OVERLAP = 75


def clean_text(text):
    """Clean copied review/forum text."""
    text = re.sub(r"\s+", " ", text)
    text = text.replace("Computer Icon", "")
    text = text.replace("Promoted", "")
    return text.strip()


def load_documents():
    """Load all .txt files from the documents folder."""
    documents = []

    for path in DOCUMENTS_DIR.glob("*.txt"):
        raw_text = path.read_text(encoding="utf-8", errors="ignore")
        cleaned_text = clean_text(raw_text)

        if cleaned_text:
            documents.append({
                "source": path.name,
                "text": cleaned_text
            })

    return documents


def chunk_text(text, source, chunk_size=CHUNK_SIZE, overlap=OVERLAP):
    """Split text into overlapping chunks."""
    chunks = []
    start = 0
    chunk_number = 0
    step = chunk_size - overlap

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if len(chunk) > 50:
            chunks.append({
                "id": f"{source}_{chunk_number}",
                "source": source,
                "chunk_number": chunk_number,
                "text": chunk
            })

        start += step
        chunk_number += 1

    return chunks


def build_chunks():
    """Load documents and produce chunks for all documents."""
    documents = load_documents()
    all_chunks = []

    for doc in documents:
        doc_chunks = chunk_text(doc["text"], doc["source"])
        all_chunks.extend(doc_chunks)

    return all_chunks


if __name__ == "__main__":
    docs = load_documents()
    chunks = build_chunks()

    print(f"Loaded {len(docs)} document(s).")
    print(f"Created {len(chunks)} chunk(s).")
    print("\nSample chunks:\n")

    for chunk in chunks[:5]:
        print("=" * 60)
        print(f"Source: {chunk['source']}")
        print(f"Chunk ID: {chunk['id']}")
        print(chunk["text"])
        print()