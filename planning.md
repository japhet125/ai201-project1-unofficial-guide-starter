# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- My domain is Data Science and Computer Science course reviews at CUNY. This knowledge is valuable because official course catalogs explain topics and credits, but they do not usually explain how difficult a course feels, how much work students actually do, how professors teach, or what students wish they knew before registering. Student reviews and discussions are harder to find because they are spread across different platforms such as Rate My Professors, Reddit, forums, and informal student comments. -->

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->



| # | Source                  | Description                                          | URL or location       |
|---|-------------------------|------------------------------------------------------|-----------------------|
| 1 |Rate My Professors       |Reviews for a CUNY computer science professor         |           location => cuny_sps_prfessors_ratings.txt                     |

| 2 |Rate My Professors       |Reviews for a CUNY data science/statistics professor  |     location => cuny_sps_charles_snead.txt    |

| 3 |Rate My professors       |CUNY reviews for  CS professors courses               |     location => cuny_sps_Alain_ledon.txt      |

| 4 |Rate my professors       |CUNY reviews for cs professors courses                |      location => cuny_sps_keri_orange_Jones.txt      
                              |
| 5 |Rate my professors       |CUNY reviews for cs professors courses                |     location => cuny_sandra_figuero.txt       |

| 6 |Rate my professor        |CUNY reviews for cs professors courses.               |      location => cuny_sps_william_JOnes_reviews.txt 
                              |
| 7 |Student forum/post       |Student opinion about workload in CS or data science courses |   location => cuny_student_sucess_redit.txt    
                              |
| 8 |Student forum/post       |Student advice about choosing professors              |  location => lehman_cs_student_comments.txt    
                              | 
| 9 |Student forum/post.      |Manually copied student comments from a course/major  |  location => cuny_redit_cs_advice.txt      |

| 10 |Student forum/post.     |Manually copied student comments from a course/major  |   location => cuny_data_science_redit.txt   |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
I will use chunks of about 400 characters.

**Overlap:**
I will use about 60 characters of overlap between chunks.
**Reasoning:**

Most course and professor reviews are short, opinion-based, and focused on one or two points such as workload, exams, grading, or teaching style. A 400–600 character chunk is large enough to keep a complete student comment together, but small enough to avoid mixing unrelated comments about different professors or courses. The overlap helps preserve context when a useful point is split near the boundary between two chunks.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
I will use all-MiniLM-L6-v2 from sentence-transformers.

**Top-k:**
I will retrieve the top 5 chunks for each query.

**Production tradeoff reflection:**
For this class project, all-MiniLM-L6-v2 is a good choice because it runs locally, is free, and is fast. For a real production system, I would compare it with larger embedding models that may have better accuracy, longer context handling, and stronger performance on noisy student review text. I would also consider latency, cost, multilingual support, and whether the model should run locally or through an API.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

#	Question	Expected answer

#1	Question => What do students say about the workload in CUNY computer science courses? Expected answer =>	The system should summarize student comments about workload, projects, assignments, and study time from the collected sources.



#2 What do students say makes a good CS or data science professor at CUNY?
Expected answer => The system should identify comments about clear explanations, feedback, grading fairness, and helpful teaching style.


#3 Are exams or projects mentioned as more difficult in the collected reviews?
Expected answer => The system should answer based only on whether the documents mention exams, projects, or both as challenging.


#4 What advice do students give before taking a difficult programming or data science course?
Expected answer => The system should return advice found in the documents, such as practicing coding, attending class, starting assignments early, or reviewing math/statistics.

#5 Which comments mention grading, feedback, or professor communication?
Expected Answer => The system should retrieve chunks that discuss grading style, feedback quality, email response, office hours, or communication.

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Student review text may be noisy, informal, or inconsistent. Some reviews may include slang, incomplete sentences, or emotional opinions, which could make retrieval less accurate.

2. Some sources may discuss multiple courses or professors in the same page. If chunks are too large, the system may mix unrelated opinions together. If chunks are too small, the system may lose important context.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

Document Ingestion
↓
Load local text files and copied review documents from the documents/ folder
↓
Chunking
↓
Split cleaned text into 400–600 character chunks with 75 character overlap
↓
Embedding + Vector Store
↓
Use all-MiniLM-L6-v2 embeddings and store chunks in ChromaDB with source metadata
↓
Retrieval
↓
Use semantic search to retrieve the top 5 most relevant chunks for a user question
↓
Generation
↓
Use Groq llama-3.3-70b-versatile to answer only from retrieved chunks with source attribution


---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**
I plan to use ChatGPT to help implement the document loading and chunking code. I will give it my Documents section, Chunking Strategy section, and Architecture diagram. I expect it to produce Python code that loads text files from the documents/ folder, cleans the text, and splits it into chunks using my chosen chunk size and overlap. I will verify the output by printing at least 5 chunks and checking that they are readable, substantive, and connected to the correct source.

**Milestone 4 — Embedding and retrieval:**
I plan to use ChatGPT to help implement embedding and retrieval with sentence-transformers and ChromaDB. I will give it my Retrieval Approach section and ask it to create code that embeds chunks, stores them with source metadata, and retrieves the top 5 chunks for a query. I will verify the output by testing at least 3 evaluation questions and checking whether the retrieved chunks are relevant.

**Milestone 5 — Generation and interface:**
I plan to use ChatGPT to help write the grounded generation prompt and a simple query interface. I will give it the assignment requirement that answers must use only retrieved chunks and include source attribution. I expect it to produce code that sends the retrieved context to Groq and returns an answer with sources. I will test it with in-scope and out-of-scope questions to make sure it does not hallucinate.
