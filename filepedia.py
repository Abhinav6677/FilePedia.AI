import streamlit as st
from app.utils import extract_text_from_pdf, extract_text_from_txt
from app.summary import get_summary
from app.qa import ask_gemini_question
from app.challenge import generate_questions, evaluate_answers

st.set_page_config(page_title="FilePedia – Document AI Assistant", layout="wide")
st.title("📚 FilePedia – Smart Document Assistant")

uploaded_file = st.file_uploader("Upload a PDF or TXT document", type=["pdf", "txt"])

if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1]

    if file_ext == "pdf":
        raw_text = extract_text_from_pdf(uploaded_file)
    else:
        raw_text = extract_text_from_txt(uploaded_file)

    st.subheader("📄 Raw Text Preview")
    st.text_area("Extracted Text:", raw_text[:3000], height=300)
    
    st.subheader("📌 Auto Summary (via Gemini API)")
    with st.spinner("Generating summary..."):
        summary = get_summary(raw_text)

    st.success("✅ Summary Ready")
    st.write(summary)
    
    st.subheader("💬 Ask Anything About the Document")

    user_question = st.text_input("Ask a question based on the uploaded content:")

    if user_question:
        with st.spinner("Thinking..."):

            answer = ask_gemini_question(document_text=raw_text, user_query=user_question)
            st.success("✅ Answer:")
            st.write(answer)
            
    st.subheader("🧩 Challenge Me")

    if st.button("Generate Questions"):
        
        with st.spinner("Generating questions..."):
            questions = generate_questions(raw_text)

        if questions:
            st.session_state["challenge_questions"] = questions

    # Show challenge questions
    if "challenge_questions" in st.session_state:
        responses = []
        
        for idx, q in enumerate(st.session_state["challenge_questions"]):
            st.markdown(f"**Question {idx + 1}**: {q}")
            user_input = st.text_input(f"Your Answer to Q{idx + 1}", key=f"user_answer_{idx}")
            responses.append(user_input)

        if st.button("Submit Answers"):
            with st.spinner("Evaluating..."):
                feedback = evaluate_answers(raw_text, st.session_state["challenge_questions"], responses)

            for i, f in enumerate(feedback):
                st.markdown(f"---\n**Q{i+1} Feedback**")
                st.write(f)




