import streamlit as st
import pandas as pd
from newsapi import NewsApiClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier

# --- 1. API SETUP ---
# Replace with your actual NewsAPI key if different
newsapi = NewsApiClient(api_key='9d4eeda9be3a408dab5a90b4844e2706')

# --- 2. AI MODEL TRAINING LOGIC ---
@st.cache_resource
def train_model():
    try:
        # Load your updated small dataset files
        fake_df = pd.read_csv('fake_small.csv')
        true_df = pd.read_csv('true_small.csv')
        
        # Assign labels
        fake_df['label'] = 'FAKE'
        true_df['label'] = 'REAL'
        
        # Combine datasets
        df = pd.concat([fake_df, true_df]).reset_index(drop=True)
        
        # Features and Labels
        x = df['title'].values.astype('U') 
        y = df['label']
        
        # UPDATED VECTORIZER: 
        # 1. ngram_range=(1, 2) helps detect word pairs like "does not"
        # 2. stop_words=None ensures words like "not" are NOT deleted
        vectorizer = TfidfVectorizer(stop_words=None, max_df=0.7, ngram_range=(1, 2))
        x_train = vectorizer.fit_transform(x)
        
        # Model Training
        model = PassiveAggressiveClassifier(max_iter=50)
        model.fit(x_train, y)
        
        return vectorizer, model
    except Exception as e:
        st.error(f"Error loading datasets: {e}. Ensure 'fake_small.csv' and 'true_small.csv' are in the folder.")
        return None, None

# Initialize the Model
vectorizer, model = train_model()

# --- 3. PROFESSIONAL UI DESIGN ---
st.set_page_config(page_title="AI News Verifier Pro", layout="wide", page_icon="🛡️")

st.title("🛡️ AI Real-Time Fake News Detector")
st.markdown("Verify news credibility using Live API or Manual Text verification.")

# Tabs for organization
tab1, tab2 = st.tabs(["🌐 Live News API", "✍️ Manual Verification"])

# --- TAB 1: LIVE NEWS API ---
with tab1:
    st.subheader("Search Current Global News")
    topic = st.text_input("Enter a topic (e.g., Cricket, Elections, Technology):", "World Events", key="live_input")
    
    if st.button("Fetch & Analyze Live News"):
        if model:
            with st.spinner('Fetching latest news...'):
                news_data = newsapi.get_everything(q=topic, language='en', sort_by='publishedAt')
                articles = news_data['articles']
                
                if articles:
                    for art in articles[:5]:
                        title = art['title']
                        input_data = vectorizer.transform([title])
                        prediction = model.predict(input_data)
                        
                        with st.expander(f"📌 {title}"):
                            if prediction == 'FAKE':
                                st.error("🚩 Result: LIKELY FAKE NEWS")
                            else:
                                st.success("✅ Result: VERIFIED REAL NEWS")
                            
                            st.write(f"**Source:** {art['source']['name']}")
                            st.markdown(f"[Read Full Article]({art['url']})")
                else:
                    st.warning("No articles found for this topic.")
        else:
            st.error("AI Model training failed.")

# --- TAB 2: MANUAL TEXT INPUT ---
with tab2:
    st.subheader("Verify Custom Text")
    user_news = st.text_area("Paste a news headline or text below:", height=150)
    
    if st.button("Verify This Text"):
        if user_news:
            if model:
                # Predicting the user-provided text
                manual_data = vectorizer.transform([user_news])
                manual_pred = model.predict(manual_data)
                
                if manual_pred == 'FAKE':
                    st.error("Prediction Result: 🚫 This appears to be FAKE NEWS.")
                else:
                    st.success("Prediction Result: ✅ This appears to be REAL NEWS.")
            else:
                st.error("Model not loaded.")
        else:
            st.warning("Please enter some text first.")

# --- SIDEBAR INFO ---
st.sidebar.title("About Project")
st.sidebar.info("""
- **Model**: Passive Aggressive Classifier
- **Features**: N-gram enabled (detects 'does not', 'is fake')
- **Real-Time**: NewsAPI Integration
""")