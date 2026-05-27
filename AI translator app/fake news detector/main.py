import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

print("--- STEP 1: Loading and Combining Fake.csv and True.csv ---")

# 1. Loading your datasets (Using exact file names with Capital F and T)
fake_df = pd.read_csv('Fake.csv', on_bad_lines='skip')
true_df = pd.read_csv('True.csv', on_bad_lines='skip')

# 2. Assigning correct labels (0 for Fake news, 1 for Real news)
fake_df['Label'] = 0
true_df['Label'] = 1

# 3. Combining both files into one single dataframe
df = pd.concat([fake_df, true_df], ignore_index=True)

# 4. Cleaning extra spaces from column names
df.columns = df.columns.str.strip()

# 5. Automatically finding the news column (checks for 'text', 'headline', or 'title')
text_col_list = [col for col in df.columns if col.lower() in ['text', 'headline', 'title']]

if not text_col_list:
    # If standard names aren't found, fallback to the first column
    text_col = df.columns[0]
else:
    text_col = text_col_list[0]

print(f"Successfully combined datasets! Total rows loaded: {len(df)}")
print(f"Using column '{text_col}' for training text.")

# Dropping missing rows to avoid empty string errors
df = df.dropna(subset=[text_col, 'Label'])
X = df[text_col].astype(str)
y = df['Label'].astype(int)

print(f"\n--- Data Distribution --- \n{y.value_counts()}")

print("\n--- STEP 2: Splitting Data into Train & Test Sets ---")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\n--- STEP 3: Transforming Text into Numbers using TF-IDF ---")
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7, min_df=2, max_features=10000)
X_train_vectorized = vectorizer.fit_transform(X_train)

print("\n--- STEP 4: Training the AI Model (Logistic Regression) ---")
model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train_vectorized, y_train)

print("\n--- STEP 5: Finding Model Accuracy & Performance ---")
X_test_vectorized = vectorizer.transform(X_test)
predictions = model.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, predictions)
print(f"🎯 Overall Model Performance Accuracy: {accuracy * 100:.2f}%")
print("\n--- Detailed Failure/Success Breakdown ---")
print(classification_report(y_test, predictions, target_names=['Fake News (0)', 'Real News (1)']))

print("\n--- STEP 6: Exporting Trained Weights to Pickled Files ---")
with open('models.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('vectorizer.pkl', 'wb') as vocab_file:
    pickle.dump(vectorizer, vocab_file)

print("\n✅ Perfect! 'models.pkl' and 'vectorizer.pkl' have been successfully generated!")