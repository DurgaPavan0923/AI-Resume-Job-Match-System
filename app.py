import streamlit as st
import os
import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sys.path.append("src")

from preprocess import clean_text
from skill_extractor import extract_skills
from job_predictor import train_model, predict_role

st.title("🚀 AI Resume Screening + Job Match System")

# Train model (only once)
if not os.path.exists("model/job_model.pkl"):
    os.makedirs("model", exist_ok=True)
    train_model()

# Load skills
with open("data/skills.txt", "r") as f:
    skill_list = f.read().splitlines()

job_desc = st.text_area("📄 Enter Job Description")

uploaded_files = st.file_uploader(
    "📂 Upload Resume (.txt)",
    type=["txt"],
    accept_multiple_files=True
)

if st.button("Analyze Resumes"):

    if not job_desc or not uploaded_files:
        st.warning("Please provide job description and resumes.")
    else:
        resumes = []
        names = []

        for file in uploaded_files:
            text = file.read().decode("utf-8")
            cleaned = clean_text(text)

            resumes.append(cleaned)
            names.append(file.name)

            st.subheader(f"📌 {file.name}")

            # Skill Extraction
            skills = extract_skills(cleaned, skill_list)
            st.write("**Extracted Skills:**", skills)

            # Job Prediction
            role = predict_role(cleaned)
            st.write("**Predicted Job Role:**", role)

            st.markdown("---")

        # Ranking System
        vectorizer = TfidfVectorizer()
        resume_vectors = vectorizer.fit_transform(resumes)
        job_vector = vectorizer.transform([clean_text(job_desc)])

        scores = cosine_similarity(job_vector, resume_vectors)[0]
        ranked = sorted(zip(names, scores), key=lambda x: x[1], reverse=True)

        st.success("✅ Resume Ranking Completed")

        for name, score in ranked:
            st.write(f"🏆 {name} → Match Score: {round(score*100,2)}%")
