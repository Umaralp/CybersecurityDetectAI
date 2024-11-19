# CybersecurityDetectAI
CybersecurityDetectAI is an NLP-based model designed to automatically classify complaints related to fraud. By preprocessing text data through tokenization, stop word removal, and stemming, it identifies the fraud type and victim. The model is evaluated using accuracy, precision, recall, and F1-score metrics.

CybersecurityDetectAI
CybersecurityDetectAI is an NLP-based model designed to automatically classify complaints related to various types of cybersecurity threats. The model uses text preprocessing techniques such as tokenization, stop word removal, stemming, and text cleaning. It then categorizes the text into relevant threat categories, helping in the identification of cybersecurity issues.

Features:
Text Preprocessing: Tokenization, stop word removal, stemming, and text cleaning to prepare data for classification.
Model Development: Uses an NLP model to classify complaints related to cybersecurity threats.

Evaluation: Performance evaluated based on accuracy, precision, recall, and F1-score metrics.

Technologies Used:
Python
Flask (for API)
scikit-learn
joblib
TF-IDF Vectorizer

Setup:
Clone the repository to your local machine.
Install the required dependencies:

pip install -r requirements.txt
Load the trained model and vectorizer.

Run the app:
python app.py

API:
The app exposes a POST endpoint at /predict, which accepts a JSON payload with a text field and returns the predicted cybersecurity threat type.
