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
        if intent == "default":
            continue  # Skip default for now
        if any(pattern in user_input for pattern in data["patterns"]):
            return data["responses"][0]  # Return first matched response
    return intents["default"]["responses"][0]  # Default fallback response

def chatbot():
    # Initialize session state
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    st.title("🤖 Simple Mental Health Chatbot")

    # Display chat history
    st.write("### 💬 Chat History")
    for chat in st.session_state.chat_history:
        st.markdown(chat)

    # Input from user
    user_input = st.text_input("You:", value=st.session_state.user_input, key="user_input")

    if st.button("Send"):
        if user_input.strip():
            # Store user message
            st.session_state.chat_history.append(f"**You:** {user_input}")

            # Generate and store bot response
            response = get_response(user_input)
            st.session_state.chat_history.append(f"**Bot:** {response}")

            # Clear the input field
            st.session_state.user_input = ""

    # Reset button
    if st.button("🔄 Reset Chat"):
        st.session_state.chat_history = []

# Make it runnable directly
if __name__ == "__main__":
    chatbot()
