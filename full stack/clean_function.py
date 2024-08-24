import re
import spacy
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