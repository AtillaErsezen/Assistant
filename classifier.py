import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

class IntentClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression()
        self.labels = []

    def load_data(self, path='intents.json'):
        with open(path, 'r') as f:
            data = json.load(f)
        texts, labels = [], []
        for intent, phrases in data.items():
            texts += phrases
            labels += [intent] * len(phrases)
        self.labels = sorted(set(labels))
        return texts, labels

    def train(self):
        X, y = self.load_data()
        X_vec = self.vectorizer.fit_transform(X)
        self.model.fit(X_vec, y)

    def predict(self, text):
        vec = self.vectorizer.transform([text])
        return self.model.predict(vec)[0]

    def save(self, model_path='model.pkl', vec_path='vectorizer.pkl'):
        with open(model_path, 'wb') as f:
            pickle.dump(self.model, f)
        with open(vec_path, 'wb') as f:
            pickle.dump(self.vectorizer, f)

    def load(self, model_path='model.pkl', vec_path='vectorizer.pkl'):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
        with open(vec_path, 'rb') as f:
            self.vectorizer = pickle.load(f)
