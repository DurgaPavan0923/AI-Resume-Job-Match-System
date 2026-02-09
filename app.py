import streamlit as st
import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.preprocess import clean_text

st.set_page_config(page_title="AI Resume Screening", layout="centered")

st.title("🧠 AI Resume Screening System")
st.write("Upload resumes and match them with a job description using NLP & ML")

# Job description input
job_desc = st.text_area("📄 Enter Job Description")

# Resume upload
uploaded_files = st.file_uploader(
    "📂 Upload Resumes (.txt files)",
    type=["txt"],
    accept_multiple_files=True
)

if st.button("🔍 Rank Resumes"):

    if not job_desc or not uploaded_files:
        st.warning("Please enter job description and upload resumes.")
    else:
        resumes = []
        names = []

        for file in uploaded_files:
            text = file.read().decode("utf-8")
            resumes.append(clean_text(text))
            names.append(file.name)

        vectorizer = TfidfVectorizer()
        resume_vectors = vectorizer.fit_transform(resumes)
        job_vector = vectorizer.transform([clean_text(job_desc)])

        scores = cosine_similarity(job_vector, resume_vectors)[0]
        ranked = sorted(zip(names, scores), key=lambda x: x[1], reverse=True)

        st.success("✅ Ranking Complete")

        for name, score in ranked:
            st.write(f"📌 **{name}** — Score: `{round(score, 2)}`")
