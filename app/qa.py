import requests

API_KEY = "AIzaSyDU2VlJnx86_atFVgmFPDUhxJcjQ1YrmS4"

def ask_gemini_question(document_text, user_query):
    # Trim text to avoid long inputs
    trimmed_text = document_text[:3000]

    prompt = f"""
    The user uploaded the following document:
    \"\"\"
    {trimmed_text}
    \"\"\"

    Now answer the following question based on the document:
    \"{user_query}\"
    """

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    { "text": prompt }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"❌ Error: {response.text}"
