import streamlit as st
from chatbot import get_response

st.title("Mental Health Chatbot 🤖💙")
st.write("Feeling stressed, anxious, or just need a laugh? Let's chat!")

user_input = st.text_input("You:", "")

if user_input:
    response = get_response(user_input)
    st.text_area("Chatbot:", value=response, height=100, max_chars=None, key=None)
