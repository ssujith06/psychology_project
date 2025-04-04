import streamlit as st

# Define intents and responses
intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Hey! How can I help?"]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "take care"],
        "responses": ["Goodbye! Have a great day!", "See you later!", "Take care!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "appreciate it"],
        "responses": ["You're welcome!", "No problem!", "Glad to help!"]
    },
    "help": {
        "patterns": ["help", "support", "assist"],
        "responses": ["Sure! What do you need help with?", "I'm here to assist you!"]
    },
    "default": {
        "responses": ["I'm sorry, I didn't understand that.", "Could you please rephrase?", "I'm not sure how to respond to that."]
    }
}

def get_response(user_input):
    """Get a response based on user input."""
    user_input = user_input.lower()
    for intent, data in intents.items():
        if any(pattern in user_input for pattern in data["patterns"]):
            return st.session_state.chat_history.append(f"Bot: {st.session_state.chat_history.append(data['responses'][0])}")
    return intents["default"]["responses"][0]

def main():
    # Initialize session state variables if they don't exist
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Streamlit app layout
    st.title("Simple Rule-Based Chatbot")
    st.write("Chat History:")
    for chat in st.session_state.chat_history:
        st.write(chat)

    # User input
    user_input = st.text_input("You:", value=st.session_state.user_input)

    if st.button("Send"):
        # Store user input in session state
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.user_input = ""  # Clear input after sending

        # Get chatbot response
        response = get_response(user_input)
        st.session_state.chat_history.append(f"Bot: {response}")

if __name__ == "__main__":
    main()
