import streamlit as st

def chatbot():
    st.title("🧠 Psychology Chatbot")
    st.write("Hi there! I'm your friendly mental health companion. Let's talk 😊")

    # ✅ Initialize session state
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # ✅ Manual intent-response pairs (you can expand this!)
    responses = {
        "hi": "Hey! How can I support you today?",
        "hello": "Hello there! How are you feeling today?",
        "i feel sad": "I'm really sorry to hear that. Want to talk about it?",
        "i'm anxious": "That’s totally okay. Try taking a few deep breaths. I’m here for you.",
        "thank you": "You're always welcome!",
        "bye": "Take care! I'm always here if you need someone to talk to."
    }

    # ✅ User input area
    user_input = st.text_input("You:", key="user_input")

    if user_input:
        # Save user message
        st.session_state.messages.append(("user", user_input))

        # Find response (case-insensitive)
        lower_input = user_input.lower()
        bot_reply = responses.get(lower_input, "I'm not sure how to respond to that, but I'm here to listen!")

        # Save bot reply
        st.session_state.messages.append(("bot", bot_reply))

        # Clear input field
        st.session_state.user_input = ""

    # ✅ Display chat history
    for sender, msg in st.session_state.messages:
        if sender == "user":
            st.markdown(f"**You:** {msg}")
        else:
            st.markdown(f"**PsychBot:** {msg}")
