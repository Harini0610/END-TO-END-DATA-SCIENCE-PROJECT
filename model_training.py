import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import joblib

# Load dataset
df = pd.read_csv('fake_or_real_news.csv')

# Prepare data
X = df['text']
y = df['label']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorization
tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_vec = tfidf.fit_transform(X_train)
X_test_vec = tfidf.transform(X_test)

# Model
model = PassiveAggressiveClassifier(max_iter=50)
model.fit(X_train_vec, y_train)

# Save
joblib.dump(model, 'fake_news_model.pkl')
joblib.dump(tfidf, 'vectorizer.pkl')
print("✅ Model and vectorizer saved.")
