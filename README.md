# 🛡️ AI Phishing Detection Web App

Python Flask Machine Learning Random Forest License Status

🔗 Link: http://127.0.0.1:5000/

---

## 🎯 Objective

This project aims to detect whether a website URL is **Phishing** or **Legitimate** using machine learning.  

Phishing websites trick users into giving sensitive information like passwords, credit card numbers, and personal data. The goal here was to build a system that can automatically identify such malicious websites using both **URL features** and a trained **Random Forest classifier**.

Explored:

- Traditional **URL feature-based detection**  
- **Rule-based heuristics** for realistic demo predictions  

The project also provides a **user-friendly web interface** where users can input URLs and get instant predictions.

---

## ⚙️ Project Scope

### 🔹 1. Phishing Detection Model
- Built a **Random Forest classifier** trained on Kaggle phishing datasets.
- Extracted multiple URL-based features (dots, dashes, length, IP in URL, etc.).
- Combined ML predictions with rule-based heuristics for more accurate real-time demo results.

### 🔹 2. Real-Time URL Analysis
- Users can enter a URL in the web app.
- The system detects suspicious patterns and predicts if it’s phishing or legitimate.
- Demo shows **safe and phishing sites** clearly.

### 🔹 3. Web Application
- Built with **Flask** and HTML/CSS for an aesthetic and user-friendly interface.
- Input field for URL and clear **result display**.
- Optional deployment online for demonstration.

---

## 🗂️ Dataset

- Dataset used: [Phishing Websites Dataset – Kaggle](https://www.kaggle.com/datasets/abhinavkumar778/phishing-sites-dataset)  
- Includes multiple features extracted from URLs labeled as **phishing** or **legitimate**.
- **Note:** Dataset is **not included in GitHub** due to size and licensing. The trained model is included in `model/phishing_model.pkl`.

---

## 🧩 Tech Stack

| Category | Tools & Frameworks |
|----------|------------------|
| Language | Python |
| Web Framework | Flask |
| ML Framework | scikit-learn (Random Forest) |
| Feature Extraction | URL parsing, feature engineering |
| Data Handling | Pandas, NumPy |
| Deployment | Local Flask server / Optional hosting |

---

## 📊 Results & Insights

| Test Input | Prediction | Observation |
|------------|-----------|------------|
| `https://www.google.com` | Legitimate | Correctly identified safe website |
| `http://account-update-google.example/signin` | Phishing | Correctly identified phishing site |
| `https://github.com` | Legitimate | Accurate prediction |
| `http://secure-login-paypal.xyz` | Phishing | Detected suspicious patterns |

- Rule-based heuristics improve demo predictions for URLs unseen during training.  
- ML model trained offline provides scalable and accurate predictions.  

---
