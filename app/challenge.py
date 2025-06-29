import requests

API_KEY = "AIzaSyDU2VlJnx86_atFVgmFPDUhxJcjQ1YrmS4"


def generate_questions(doc_text):
    trimmed = doc_text[:3000]
    prompt = f"""
You are a helpful AI assistant. Read the document below and generate 3 unique logic-based or comprehension-based questions that require inference — not factual recall.

Document:
\"\"\"
{trimmed}
\"\"\"

Your task: Return exactly 3 numbered questions. Avoid blank lines, and do not return empty questions.

Format:
1. [question]
2. [question]
3. [question]
"""

    output = ask_gemini(prompt)

    # Split and clean
    questions = [line.strip()[2:].strip() for line in output.split("\n") if line.strip().startswith(("1.", "2.", "3.")) and len(line.strip()) > 3]

    return questions if len(questions) == 3 else ["(❌ Failed to generate 3 valid questions)"]


    return ask_gemini(prompt)

def evaluate_answers(doc_text, questions, answers):
    prompt = f"""
You're a teaching assistant AI. Evaluate the user's answers to the questions below based on the document content.

Your task:
- For each answer, clearly state: Correct / Partially Correct / Incorrect.
- Provide a 1-2 sentence explanation referencing the document.

Document:
\"\"\"
{doc_text[:3000]}
\"\"\"

Evaluate these:

"""

    for i, (q, a) in enumerate(zip(questions, answers)):
        prompt += f"\nQ{i+1}: {q}\nUser Answer: {a}\n"

    result = ask_gemini(prompt)

    # Post-process: Extract feedback only for Q1, Q2, Q3
    feedback = []
    for i in range(1, len(questions) + 1):
        start = result.find(f"Q{i}:")
        end = result.find(f"Q{i+1}:", start) if i < len(questions) else len(result)
        q_feedback = result[start:end].strip() if start != -1 else "❌ Feedback missing."
        feedback.append(q_feedback)

    return feedback
 # Split into feedback per question

def ask_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [{ "text": prompt }]
            }
        ]
    }

    res = requests.post(url, headers=headers, json=payload)

    if res.status_code == 200:
        return res.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return [f"❌ Error: {res.text}"]
