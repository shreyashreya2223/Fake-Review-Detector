from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Load and clean dataset
df = pd.read_csv("fake_reviews_dataset.csv")
df.columns = df.columns.str.strip()

X = df['text_']
y = df['label']

# Vectorize text
vectorizer = TfidfVectorizer()
X_vect = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vect, y)

# Routes
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/learn')
def learn():
    return render_template("learn.html")

@app.route('/tips')
def tips():
    return render_template("tips.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/faq')
def faq():
    return render_template("faq.html")

@app.route('/credits')
def credits():
    return render_template("credits.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review = data.get('review')

    if not review:
        return jsonify({"error": "No review provided"}), 400

    review_vect = vectorizer.transform([review])
    prediction = model.predict(review_vect)[0]

    result = "Fake" if prediction == 1 else "Genuine"
    return jsonify({"prediction": result})

# Correct startup
if __name__ == '__main__':
    app.run(debug=True)
