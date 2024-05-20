import streamlit as st
import pickle
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('stopwords')

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('spam_model.pkl', 'rb'))

ps = PorterStemmer()

def transform_text(text):
    text = text.lower() # convert to lower case
    text = nltk.word_tokenize(text) # tokenize into words
    
    y = []
    for i in text: 
        if i.isalnum() and i not in string.punctuation and i not in stopwords.words():  # only alllowing alphanumeric words without stop words
            y.append(ps.stem(i)) # appending after stemming the word

    return " ".join(y) 

st.title('Email/SMS Spam Classifier')

input_sms = st.text_input('Enter the message')

if st.button('predict'):
    transformed_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]

    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")

