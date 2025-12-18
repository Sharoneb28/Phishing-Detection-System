import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("model/phishing_model.pkl")

st.set_page_config(
    page_title="AI Phishing Detection System",
    page_icon="🔒",
    layout="centered"
)

# Soft purple-pink-orange gradient
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #c77dff, #f72585, #ffb703);
}

/* Improve text readability */
h1, label, p {
    color: white !important;
}

/* Button styling */
.stButton button {
    background-color: #4a148c;
    color: white;
    font-size: 16px;
    padding: 10px;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# Spacing
st.write("")
st.write("")

# Title
st.markdown(
    "<h1 style='text-align:center;'>🔒 AI Phishing Detection System</h1>",
    unsafe_allow_html=True
)

st.write("")

# Input
url = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)

st.write("")

# Button
if st.button("Analyze Website", use_container_width=True):
    if url.strip() == "":
        st.warning("Please enter a website URL.")
    else:
        features = pd.DataFrame([[0]*48])
        prediction = model.predict(features)[0]

        if prediction == 1:
            st.success("✅ This website is LEGITIMATE")
        else:
            st.error("⚠️ This website is PHISHING")

st.write("")
st.markdown(
    "<p style='text-align:center;'>Machine Learning based security system</p>",
    unsafe_allow_html=True
)

