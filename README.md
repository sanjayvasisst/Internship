# Spam Classification Project

This project classifies emails or SMS messages as **Spam** or **Not Spam** using Machine Learning (SVM model).

##  Project Overview
- **Algorithm:** Support Vector Machine (SVM)
- **Feature Extraction:** TF-IDF Vectorization
- **Dataset:** `spam.csv`
- **Frontend:** Streamlit app for interactive predictions

## Model Info
- TF-IDF vectorizer converts text into numerical features.
- Trained SVM classifier predicts whether a message is spam.

## Files Included
- `spam_classification.ipynb` – Full notebook (EDA, preprocessing, training, evaluation)
- `main.py` – Streamlit app for real-time input
- `model.pkl` – Trained model
- `vectorizer.pkl` – TF-IDF vectorizer
- `spam.csv` – Dataset
- `requirements.txt` – Dependencies
- `README.md` – Documentation

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```
2. Enter a message to test and view predictions.

##  Author
**Sanjay Nagda**
*BCA Student | Aspiring AI/ML Engineer*
*sanjaynagda@gmail.com.com*
