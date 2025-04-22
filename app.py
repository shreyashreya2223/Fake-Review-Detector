from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Load and clean dataset
df = pd.read_csv("fake_reviews_dataset.csv")
df.columns = df.columns.str.strip()  # Clean whitespace
print("CSV Columns:", df.columns.tolist())  # Optional: Debug

# Use the correct column name
X = df['text_']
y = df['label']

# Vectorize the review text
vectorizer = TfidfVectorizer()
X_vect = vectorizer.fit_transform(X)

# Train the model
model = LogisticRegression()
model.fit(X_vect, y)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    review = request.json.get("review")
    
    if not review:
        return jsonify({"error": "No review provided"}), 400

    review_vect = vectorizer.transform([review])
    prediction = model.predict(review_vect)[0]

    result = "Fake" if prediction == 1 else "Genuine"
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(debug=True)
