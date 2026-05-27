import streamlit as st
import pickle

# 1. Load the successfully trained model and vectorizer
with open('models.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Web app interface setup
st.title("Accurate Fake News Detector 🕵️‍♂️")
st.write("This app uses your trained True/Fake dataset to detect misinformation.")

# Text area for user input
user_input = st.text_area("Paste News Content Here:", height=200)

if st.button("Predict"):
    if user_input.strip():
        # Transform and predict using the loaded model
        data = vectorizer.transform([user_input])
        prediction = model.predict(data)[0]
        
        # Exact Label Logic based on your training: 0 = Fake, 1 = Real
        if prediction == 0:
            st.error("🚨 Warning: This is FAKE News!")
        else:
            st.success("✅ Success: This is REAL News!")
    else:
        st.warning("Please enter some text to predict.")