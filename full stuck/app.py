from flask import Flask, render_template, request, jsonify
import joblib
import re
import spacy

app = Flask(__name__)

# Load your model
model = joblib.load('best_model/logistic_regression.pkl')

# Load the SpaCy model for text processing
nlp = spacy.load("en_core_web_sm")

def clean(doc):
    # Remove punctuation
    doc = re.sub(r'[^\w\s]', '', doc)
    # Convert to lowercase
    doc = doc.lower()
    # Tokenize and lemmatize
    doc = nlp(doc)
    lemmatized_tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    # Join tokens back into a string
    return " ".join(lemmatized_tokens)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('text')
    cleaned_text = clean(text)
    
    # Predict the class
    prediction = model.predict([cleaned_text])[0]
    
    # Map the prediction to a sentiment label
    sentiment_map = {
        1: "Positive",
        2: "Neutral",
        3: "Negative"
    }
    sentiment = sentiment_map.get(prediction, "Unknown")
    
    # Render the result in the template
    return render_template('index.html', prediction=sentiment)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
