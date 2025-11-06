import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for word in text:
        if word.isalnum():
            y.append(word)

    text = y[:]
    y.clear()

    for word in text:
        if word not in stopwords.words('english') and word not in string.punctuation:
            y.append(word)

    text = y[:]
    y.clear()

    for word in text:
        y.append(ps.stem(word))

    return " ".join(y)

# Streamlit UI
st.title("Email / SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):    
    transformed_sms = transform_text(input_sms)     
    vector_input = tfidf.transform([transformed_sms]).toarray()    
    result = model.predict(vector_input)[0]
     
    if result == 1:
        st.error("Spam Message Detected!")
    else:
        st.success("message is Not Spam.")
