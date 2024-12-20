# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yP24Y4qBHApNjcQtIKJZPTSWpoKpHSSr
"""

from flask import Flask, request, jsonify
import joblib

# Load the saved model and vectorizer
model = joblib.load('text_classification_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Initialize Flask app
app = Flask(__name__)

# Define the /predict route to handle both JSON and form data
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if the request content type is JSON
        if request.is_json:
            # Get the input text from the request (for JSON data)
            data = request.get_json()
            text = data.get("text", "")
        else:
            # Get the input text from the form (for form data)
            text = request.form.get("text", "")

        # Transform the text using the vectorizer
        X = vectorizer.transform([text])

        # Make prediction
        prediction = model.predict(X)[0]

        # Return the prediction
        return jsonify({"prediction": prediction})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
