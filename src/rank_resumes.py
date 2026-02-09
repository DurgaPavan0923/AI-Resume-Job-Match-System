import joblib
from sklearn.metrics.pairwise import cosine_similarity
from src.preprocess import clean_text

vectorizer = joblib.load("model/vectorizer.pkl")
resume_vectors = joblib.load("model/resume_vectors.pkl")

with open("data/job_description.txt", "r", encoding="utf-8") as f:
    job_desc = clean_text(f.read())

job_vector = vectorizer.transform([job_desc])
scores = cosine_similarity(job_vector, resume_vectors)

ranked = sorted(list(enumerate(scores[0])), key=lambda x: x[1], reverse=True)

print("\n📊 Resume Ranking:")
for idx, score in ranked:
    print(f"Resume {idx+1} → Score: {round(score, 2)}")
