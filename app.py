import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
vs = SentimentIntensityAnalyzer()
st.title('Sentiment Analysis')
ip = st.text_input("Enter the review")
pred = vs.polarity_scores(ip)['compound']
if pred >= 0.4:
  op = "Positive review"
elif pred <= -0.05:
  op = "Negative review"
else:
  op = "Neutral review"

if st.button('Predict'):
  st.title(op)
