import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def train_model():
    data = pd.read_csv("data/job_roles.csv")
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data["resume_text"])
    y = data["job_role"]

    model = MultinomialNB()
    model.fit(X, y)

    joblib.dump(model, "model/job_model.pkl")
    joblib.dump(vectorizer, "model/job_vectorizer.pkl")

def predict_role(text):
    model = joblib.load("model/job_model.pkl")
    vectorizer = joblib.load("model/job_vectorizer.pkl")

    text_vec = vectorizer.transform([text])
    return model.predict(text_vec)[0]
