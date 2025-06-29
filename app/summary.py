import requests
import streamlit as st

API_KEY = "AIzaSyDU2VlJnx86_atFVgmFPDUhxJcjQ1YrmS4"

@st.cache_data(show_spinner=False)
def get_summary(text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Summarize the following document in under 150 words:\n\n{text[:3000]}"
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"❌ Failed: {response.text}"
