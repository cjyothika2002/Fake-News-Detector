# Hybrid Fake News Detection & Fact-Checking System

This project is a Flask-based web application that detects whether a news paragraph is **Real** or **Fake** using a **hybrid approach**:

- Machine Learning (TF-IDF + Multinomial Naive Bayes)
- Rule-based Fact Checking Layer

The system overcomes the limitation of pure ML models that fail when fake news is written in a formal, realistic style.

---

##  Features

- Detects fake news using NLP and ML
- Rule-based engine to catch logically impossible claims
- Confidence score for ML predictions
- Clean glassmorphism UI
- Ready for deployment on cloud platforms

---

##  Architecture

User Input  
→ Text Cleaning  
→ Fact-Check Rules  
→ ML Prediction  
→ Final Result

---

## Tech Stack

- Python
- Flask
- Scikit-learn
- TF-IDF Vectorizer
- Multinomial Naive Bayes
- HTML, CSS, JavaScript

---

## 📂 Project Structure
