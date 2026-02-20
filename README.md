# 🚀 AI Resume Screening & Job Match System

An AI-powered intelligent recruitment assistant that automates resume screening using **Natural Language Processing (NLP)** and **Machine Learning**.

Built specifically for:

- 🎓 Campus Placement Automation  
- 🏢 HR Resume Shortlisting  
- 🚀 Startup Hiring  
- 🤖 AI-Based Recruitment Systems  

---

## 📌 Project Overview

This system analyzes uploaded resumes and matches them against a given job description.

It performs:

- Resume preprocessing using NLP
- Skill extraction
- Job role prediction using Naive Bayes
- Resume ranking using TF-IDF + Cosine Similarity
- Match score calculation (%)

The system reduces manual screening effort and increases hiring efficiency using data-driven decision-making.

---

## 🔥 Key Features

- 📄 Job Description Input  
- 📂 Upload Multiple Resumes (.txt)  
- 🧹 Resume Text Preprocessing  
- 🛠️ Technical Skill Extraction  
- 🎯 Job Role Prediction (Naive Bayes)  
- 📊 TF-IDF Vectorization  
- 📈 Cosine Similarity Ranking  
- 🌐 Interactive Streamlit Interface  

---

## 🧠 How It Works

1. User enters a job description.
2. User uploads one or more resume files (.txt).
3. The system:
   - Cleans and preprocesses text (tokenization, stopword removal, normalization).
   - Extracts relevant skills.
   - Converts text to TF-IDF vectors.
   - Calculates cosine similarity between resumes and job description.
   - Predicts suitable job role using Naive Bayes classifier.
4. Resumes are ranked based on match percentage.
5. Results are displayed in the Streamlit interface.

---

## 🏗️ System Architecture

```

Job Description
     ↓
Resume Upload (.txt)
     ↓
Text Preprocessing (NLTK)
     ↓
Skill Extraction
     ↓
TF-IDF Vectorization
     ↓
Cosine Similarity
     ↓
Naive Bayes Role Prediction
     ↓
Ranking & Match Score Output

```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Programming Language | Python |
| NLP | NLTK |
| Machine Learning | Scikit-learn |
| Model Used | Multinomial Naive Bayes |
| Vectorization | TF-IDF |
| Similarity Metric | Cosine Similarity |
| Frontend Framework | Streamlit |

---

## 📂 Project Structure

```

AI-Resume-Job-Match-System/
│
├── app.py
├── model/
│   └── naive_bayes_model.pkl
├── utils/
│   ├── preprocess.py
│   ├── skill_extractor.py
│   └── similarity.py
├── assets/
│   └── screenshots/
├── requirements.txt
└── README.md

````

---

## ▶️ How to Run Locally

### 1️⃣ Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Job-Match-System.git
cd AI-Resume-Job-Match-System
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
streamlit run app.py
```

Open your browser and go to:

```
http://localhost:8501
```

---

## 🎯 Placement-Oriented Use Case

This project is ideal for:

* University placement cells
* HR departments
* AI-based ATS systems
* Recruitment startups
* Automated resume shortlisting systems

It demonstrates practical implementation of NLP + ML in a real-world industry problem.

---

## 🔮 Future Enhancements

* PDF Resume Parsing
* Advanced Skill Extraction using NER
* BERT-based Resume Matching
* ATS Score Calculation
* Recruiter Dashboard
* Database Integration
* Cloud Deployment (Streamlit Cloud / Render)
* Authentication System (Admin Login)

---

## 💡 Why This Project Stands Out

✔ Real-world application

✔ Combines NLP + Machine Learning

✔ Placement-ready AI project

✔ Easily extendable to Deep Learning

✔ Strong portfolio addition
