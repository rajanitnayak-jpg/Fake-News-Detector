import pandas as pd
import requests
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# --- 1. CONFIGURATION ---
API_KEY = "9d4eeda9be3a408dab5a90b4844e2706"

def check_real_time_news(headline):
    """NewsAPI moolaka news verify madalu"""
    try:
        url = f"https://newsapi.org{headline}&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        if data.get('totalResults', 0) > 0:
            return True 
    except:
        return False
    return False

# --- 2. DATASET PREPARATION & TRAINING ---
def setup_model():
    try:
        print("Reading True.csv and Fake.csv...")
        # Eradu files load madi
        true_df = pd.read_csv('True.csv')
        fake_df = pd.read_csv('Fake.csv')

        # Label set madi (1 for True, 0 for Fake)
        true_df['label'] = 'TRUE'
        fake_df['label'] = 'FAKE'

        # Eradanna ondu madi (Combine)
        df = pd.concat([true_df, fake_df]).reset_index(drop=True)
        
        # Column names check (Usually 'title' or 'text')
        # Nimma file alli 'title' idre 'title' balasi
        column_to_use = 'title' if 'title' in df.columns else 'text'
        
        x = df[column_to_use]
        y = df['label']

        # Split data
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=7)

        # Vectorization
        tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
        tfidf_train = tfidf_vectorizer.fit_transform(x_train)
        tfidf_test = tfidf_vectorizer.transform(x_test)

        # Model Building
        pac = PassiveAggressiveClassifier(max_iter=50)
        pac.fit(tfidf_train, y_train)

        # Accuracy
        y_pred = pac.predict(tfidf_test)
        print(f'✅ Model Accuracy: {round(accuracy_score(y_test, y_pred)*100, 2)}%')

        return pac, tfidf_vectorizer

    except Exception as e:
        print(f"❌ Error: {e}")
        return None, None

# --- 3. RUNNING THE APP ---
if __name__ == "__main__":
    model, vectorizer = setup_model()

    if model:
        print("\n" + "="*40)
        print("🚀 REAL-TIME FAKE NEWS DETECTOR READY")
        print("="*40)
        
        while True:
            user_input = input("\nEnter News Headline (or 'exit' to quit): ")
            if user_input.lower() == 'exit': break

            # AI Prediction
            vec_input = vectorizer.transform([user_input])
            ai_pred = model.predict(vec_input)[0]

            if ai_pred == 'FAKE':
                print("⏳ AI thinks it's Fake... Cross-checking with NewsAPI...")
                if check_real_time_news(user_input):
                    print("RESULT: ✅ TRUE NEWS (Verified by Real-time Sources)")
                else:
                    print("RESULT: ❌ FAKE NEWS (No trusted sources found)")
            else:
                print("RESULT: ✅ TRUE NEWS")