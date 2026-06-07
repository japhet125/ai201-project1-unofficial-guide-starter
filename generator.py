import os
from dotenv import load_dotenv
from groq import Groq

from retriever import retrieve, ingest_to_chroma

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = "llama-3.3-70b-versatile"

client = Groq(api_key=GROQ_API_KEY)


def generate_response(query):
    retrieved_chunks = retrieve(query, n_results=5)

    if not retrieved_chunks:
        return "I could not find enough information in the documents to answer that question."

    relevant_chunks = [
        chunk for chunk in retrieved_chunks
        if chunk["distance"] <= 0.5
    ]

    if not relevant_chunks:
        return "I could not find enough information in the documents to answer that question."

    context_parts = []

    for chunk in relevant_chunks:
        context_parts.append(
            f"[Source: {chunk['source']} | Distance: {chunk['distance']:.4f}]\n"
            f"{chunk['text']}"
        )

    context = "\n\n---\n\n".join(context_parts)

    system_message = """
You are The Unofficial Guide, a grounded student-advice assistant.

Answer the user's question using only the retrieved document context.
Do not use outside knowledge.
Do not invent facts.
If the documents do not contain enough information, say:
"I could not find enough information in the documents to answer that question."

Always mention the source file(s) used in the answer.
"""

    user_message = f"""
User question:
{query}

Retrieved document context:
{context}
"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    ingest_to_chroma()

    question = input("Ask a question: ")
    answer = generate_response(question)

    print("\nAnswer:\n")
    print(answer)