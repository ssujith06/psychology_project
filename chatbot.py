import streamlit as st

def chatbot():
    st.subheader("Mental Health Chatbot")
    st.write("I'm here to chat! Ask me anything.")
    user_input = st.text_input("You:")
    
    if st.button("Send"):
        response = chatbot_response(user_input)
        st.text_area("Bot:", value=response, height=100, max_chars=None)

def chatbot_response(text):
    responses = {
        "hello": "Hey there! How can I cheer you up today?",
        "sad": "It's okay to feel sad. Want to talk about it?",
        "stress": "Take a deep breath. Everything will be okay!",
        "joke": "Why did the student eat his homework? Because his teacher said it was a piece of cake!",
        "bye": "Goodbye! Stay positive!"
    }
    text = text.lower()
    for key in responses.keys():
        if key in text:
            return responses[key]
    return "I'm here to listen. Tell me more."
