from flask import Flask, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained ML model
model = joblib.load("model/phishing_model.pkl")

# IMPORTANT: must match model.n_features_in_
NUM_FEATURES = model.n_features_in_

# ---------- Rule-based phishing detection (Demo Logic) ----------
def is_suspicious_url(url):
    suspicious_keywords = [
        "login", "signin", "verify", "update", "secure",
        "account", "bank", "paypal", "google", "apple"
    ]

    if url.count('.') > 4:
        return True
    if "@" in url:
        return True
    if url.startswith("http://"):
        return True
    if "-" in url:
        return True

    for word in suspicious_keywords:
        if word in url.lower():
            return True

    return False


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Phishing Detection</title>
        <style>
            body {
                background: linear-gradient(135deg, #1d2671, #c33764);
                font-family: Arial, sans-serif;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
            }
            .card {
                background: white;
                padding: 35px;
                border-radius: 18px;
                width: 420px;
                text-align: center;
                box-shadow: 0 15px 30px rgba(0,0,0,0.3);
            }
            h2 {
                margin-bottom: 20px;
                color: #333;
            }
            input {
                width: 100%;
                padding: 12px;
                border-radius: 8px;
                border: 1px solid #ccc;
                margin-bottom: 20px;
                font-size: 14px;
            }
            button {
                width: 100%;
                padding: 12px;
                background: #1d2671;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 15px;
                cursor: pointer;
            }
            button:hover {
                background: #16205c;
            }
            .footer {
                margin-top: 15px;
                font-size: 12px;
                color: #777;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>🔐 AI Phishing Detection System</h2>
            <form method="post" action="/predict">
                <input type="text" name="url" placeholder="Enter website URL" required>
                <button type="submit">Analyze Website</button>
            </form>
            <div class="footer">Machine Learning based security system</div>
        </div>
    </body>
    </html>
    """


@app.route("/predict", methods=["POST"])
def predict():
    url = request.form["url"]

    # Rule-based detection (for realistic demo)
    if is_suspicious_url(url):
        result = "⚠️ Phishing Website Detected"
        color = "red"
    else:
        # Dummy ML prediction (feature extraction is future work)
        features = np.zeros(NUM_FEATURES).reshape(1, -1)
        prediction = model.predict(features)[0]

        if prediction == -1:
            result = "⚠️ Phishing Website Detected"
            color = "red"
        else:
            result = "✅ Legitimate Website"
            color = "green"

    return f"""
    <html>
    <head>
        <title>Result</title>
        <style>
            body {{
                background: linear-gradient(135deg, #1d2671, #c33764);
                font-family: Arial;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
            }}
            .card {{
                background: white;
                padding: 35px;
                border-radius: 18px;
                width: 420px;
                text-align: center;
                box-shadow: 0 15px 30px rgba(0,0,0,0.3);
            }}
            h2 {{
                color: {color};
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                text-decoration: none;
                color: #1d2671;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>{result}</h2>
            <a href="/">Check Another URL</a>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
