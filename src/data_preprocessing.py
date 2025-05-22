import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def load_and_prepare_data():
    # Carrega dados
    df = pd.read_csv('data/processed/nlp_chatbot_dataset.csv')

    # Preprocessamento
    df['pergunta'] = df['pergunta'].apply(preprocess_text)
    X = df['pergunta']
    y = df['categoria']

    # TF-IDF
    vectorizer = TfidfVectorizer()
    X_tfidf = vectorizer.fit_transform(X)

    # Encode labels
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    return X_tfidf, y_encoded, vectorizer, label_encoder
