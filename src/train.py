import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from src.preprocess import clean_text

resume_folder = "data/resumes"

resumes = []
for file in os.listdir(resume_folder):
    with open(os.path.join(resume_folder, file), 'r', encoding='utf-8') as f:
        resumes.append(clean_text(f.read()))

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(resumes)

joblib.dump(vectorizer, "model/vectorizer.pkl")
joblib.dump(X, "model/resume_vectors.pkl")

print("Model trained successfully!")
