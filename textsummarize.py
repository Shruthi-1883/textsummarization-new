import streamlit as st
from gensim.summarization import summarize
text=st.text_area("Enter the para you want to summarize:")
button=st.button("Submit")
if button:
  summary = summarize(text, ratio=0.4)  
  st.text(summary)




