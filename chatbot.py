import streamlit as st

# Ensure session state is initialized before accessing it
if "messages" not in st.session_state:
    st.session_state.messages = []  # Initialize chat history

def chatbot_response(text):
    responses = {
        "hello": "Hey there! How can I cheer you up today? 😊",
        "sad": "It's okay to feel sad. Want to talk about it? 💙",
        "stress": "Take a deep breath. Everything will be okay! 🌿",
        "joke": "Why did the student eat his homework? Because his teacher said it was a piece of cake! 😂",
        "bye": "Goodbye! Stay positive! 😊"
    }

    for key in responses.keys():
        if key in text:
            return responses[key]

    return "I'm here to listen. Tell me more. 🤗"

def chatbot():
    st.title("🛏️ Hostel Management System")
    st.subheader("💬 Mental Health Chatbot")

    # Display chat history
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"👤 **You:** {msg['content']}")
        else:
            st.markdown(f"🤖 **Bot:** {msg['content']}")

    user_input = st.text_input("Type your message:", key="chat_input")

    if st.button("Send") and user_input.strip():
        # Save user's message
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Get bot's response
        response = chatbot_response(user_input.lower())

        # Save bot's response
        st.session_state.messages.append({"role": "bot", "content": response})

        # Refresh the chat UI
        st.experimental_rerun()

if __name__ == "__main__":
    chatbot()
