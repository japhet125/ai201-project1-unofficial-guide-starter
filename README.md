# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

     My domain is Data Science and Computer Science course reviews at CUNY. This knowledge is valuable because official course catalogs explain topics and credits, but they do not usually explain how difficult a course feels, how much work students actually do, how professors teach, or what students wish they knew before registering. Student reviews and discussions are harder to find because they are spread across different platforms such as Rate My Professors, Reddit, forums, and informal student comments.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->



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

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
I will use chunks of about 400–600 characters.

**Overlap:**
I will use about 75 characters of overlap between chunks.

**Why these choices fit your documents:**
Most course and professor reviews are short, opinion-based, and focused on one or two points such as workload, exams, grading, or teaching style. A 400–600 character chunk is large enough to keep a complete student comment together, but small enough to avoid mixing unrelated comments about different professors or courses. The overlap helps preserve context when a useful point is split near the boundary between two chunks.


**Final chunk count:**
61 chunks

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**
llama-3.3-70b-versatile

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
   system_message = """
You are The Unofficial Guide, a grounded student-advice assistant.

Answer the user's question using only the retrieved document context.
Do not use outside knowledge.
Do not invent facts.
If the documents do not contain enough information, say:
"I could not find enough information in the documents to answer that question."

Always mention the source file(s) used in the answer.
"""


**How source attribution is surfaced in the response:**
source attribution is surfaced it the response at the bottom .txt

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 |Query: What do students say about
 the workload in the CUNY SPS
  Data Science program? 

Top retrieved chunk:
Source: cuny_data_science_redit.txt
Distance: 0.3932
Expected answer: was given the exact answer.
Retrieval quality: Relevant

Explanation:
The top chunk is relevant because it directly discusses the CUNY SPS Master’s in Data Science program and mentions that the program is challenging without prior coding experience, time consuming, and includes homework, study sessions, readings, and meetups.

Response accuracy: accurate
| 2 | Query: What do students say about William Jones?
Ezxpected answer: that's not quiet the answer i was expecting cause there are two Jones, William Jones and Kerri Jones and the system gave me the Kerri Jones review.

System response:According to the retrieved document context from the file 'cuny_sps_keri_orange_Jones.txt', students have very positive things to say about Professor Jones. One student states that Professor Jones is "by far the best professor I have ever had" and describes her as "accommodating", "cool", "funny", "inspirational", and mentions that she gives "amazing lectures". However, it does not mention a William Jones, but rather a Professor Jones, who appears to be a female professor. 

Source: cuny_sps_keri_orange_Jones.txt

Retrieval quality: Partially relevant but mixed not the right person
Response accuracy : Partially accurate



| 3 | Query: Which CUNY school do students recommend for Computer Science?

Expected Answer: The system gave the Expected answer

system response: Based on the retrieved document context from 'cuny_redit_cs_advice.txt', some students recommend Queens College for its Computer Science program. One user mentions, "I think Queens has the best CS program." 

Additionally, Brooklyn College is mentioned as being "decent" for Computer Science, and John Jay College is noted for being good for cybersecurity. However, it's essential to note that opinions on the best CUNY school for Computer Science vary among students, and some express dissatisfaction with their experiences at certain schools, such as CCNY and Hunter. 

Source: cuny_redit_cs_advice.txt
Retrieval quality: Relevant
Response accuracy: Accurate

| 4 | Query: Which comments mention grading, feedback, or professor communication?
Expected Answer: Gradings and feeback from professors
System response: I could not find enough information in the documents to answer that question.

Retrieval quality: Partially relevant
Response accuracy: Accurate
| 5 | Query: Are exams or projects mentioned as more difficult in the collected reviews?
Expected answer:  not what was expected but i guess the reviews did not include those details since I filtered the reviews

System Response: I could not find enough information in the documents to answer that question.
Retrieval quality: Partially relevant
Response accuracy: Partially accurate



**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**
Query: Are exams or projects mentioned as more difficult in the collected reviews?

this question failed because i copied only the reviews of the proffesors and sellected few proffesors to get their reviews with what student says about them and those reviews did not include the difficulties section.

**What the system returned:**
System response: I could not find enough information in the documents to answer that question.

**Root cause (tied to a specific pipeline stage):**
less details

**What you would change to fix it:**
I would have to include all reviews comments and make sure it cover everything and also reframe my question

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
planning.md was the main job and spending time planning was worhty it gives a workload of how to procceed. what answer to ask? how to do the chunking and the overlapping.

**One way your implementation diverged from the spec, and why:**
yes during implementation I have to change my domain cause not all domain were available with api or clean structure.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:* i gave AI the project structure and ask how can proceed with it
- *What it produced:* it produced the workload where to start adn where to finish
- *What I changed or overrode:* I followed the steps

**Instance 2**

- *What I gave the AI:* I run to bug and can figure it out the chunk and the overlopping
- *What it produced:* suggested chunk strategy and overlopping ranges
- *What I changed or overrode:* I have changing some chunk size and overlop ranges
