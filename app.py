import gradio as gr

from generator import generate_response
from retriever import ingest_to_chroma

# Make sure the database is populated
ingest_to_chroma()


def answer_question(question):
    if not question.strip():
        return "Please enter a question."

    return generate_response(question)


demo = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Ask a question about CUNY CS or Data Science programs..."
    ),
    outputs=gr.Textbox(lines=10),
    title="The Unofficial Guide",
    description="""
Ask questions about CUNY Computer Science and Data Science programs,
professors, workload, student experiences, and advice based on collected reviews.
"""
)

if __name__ == "__main__":
    demo.launch()