from flask import Flask, render_template, request
import pickle
import re
from facts import rule_based_check   # ← using YOUR facts.py

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

def clean(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    return text

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/how")
def how():
    return render_template("how.html")

@app.route("/predict", methods=["POST"])
def predict():
    news = request.form["news"]

    # ✅ Clean
    news_clean = clean(news)

    # ✅ RULE CHECK FIRST (your facts.py runs here)
    if rule_based_check(news_clean):
        result = "🔴 FAKE NEWS (Fact rule triggered)"
        return render_template(
            "index.html",
            prediction_text=result,
            news_text=news
        )

    # ✅ ML AFTER rule check
    vec = vectorizer.transform([news_clean])
    pred = model.predict(vec)[0]
    proba = model.predict_proba(vec)[0]
    confidence = round(max(proba) * 100, 2)

    if pred == 0:
        result = f"🔴 FAKE NEWS (ML) — Confidence: {confidence}%"
    else:
        result = f"🟢 REAL NEWS (ML) — Confidence: {confidence}%"

    return render_template(
        "index.html",
        prediction_text=result,
        news_text=news
    )

if __name__ == "__main__":
    app.run(debug=True)