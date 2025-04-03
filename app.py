import os
import sys
import subprocess

# Ensure correct Python path is used
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Install nltk if not found
try:
    import nltk
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "nltk"])
    import nltk

# Download required NLTK data
nltk.download('vader_lexicon')

import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="🤖 Fun Mental Health Chatbot", layout="centered")

st.title("🤖 Chat with Me - Your Friendly AI!")
st.write("Hey! I'm here to talk, joke, and help with stress. Ask me anything!")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Type a message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display chatbot response
    with st.chat_message("assistant"):
        st.markdown(response)
