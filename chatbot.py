import streamlit as st
import re

# Helper: Simple sentiment awareness
def detect_sentiment(user_input):
    if re.search(r'\b(suicidal|hopeless|worthless)\b', user_input):
        return "crisis"
    elif re.search(r'\b(sad|anxious|depressed|tired|lonely)\b', user_input):
        return "negative"
    elif re.search(r'\b(happy|grateful|okay|better)\b', user_input):
        return "positive"
    else:
        return "neutral"

# Helper: Generate bot response
def generate_response(user_input):
    user_input = user_input.lower()

    # Sentiment detection
    sentiment = detect_sentiment(user_input)

    if sentiment == "crisis":
        return ("I'm really concerned about your safety. "
                "Please consider contacting a professional or reaching out to a crisis line immediately. "
                "[Click here for help](https://findahelpline.com/)")

    # Intent matching
    if re.search(r'\bstress(ed)?\b', user_input):
        return "Stress is tough. Would you like a few strategies to cope?"
    elif re.search(r'\banxiety\b|\bpanic\b', user_input):
        return "Anxiety can be draining. Grounding exercises might help. Want to try one together?"
    elif re.search(r'\bsleep\b|\binsomnia\b', user_input):
        return "I can suggest a bedtime routine or a simple breathing exercise to help with sleep. Interested?"
    elif re.search(r'\bsad\b|\blonely\b|\bdepressed\b', user_input):
        return "You’re not alone. I’m here for you. Want to talk more or try a mood-lifting activity?"
    elif re.search(r'\b(breathing|relax|calm|cope)\b', user_input):
        return "Let's take a moment. Inhale for 4 seconds, hold for 4, exhale for 4. Repeat a few times with me."
    else:
        return "I'm listening. Tell me more about what's on your mind."

# Optional suggestions
def show_coping_strategies():
    with st.expander("💡 Coping Strategies"):
        st.markdown("""
        - Try journaling your thoughts.
        - Take a short walk in fresh air.
        - Do 5-minute guided meditation.
        - Limit social media when overwhelmed.
        - Talk to someone you trust.
        """)

def show_relaxation_exercises():
    with st.expander("🧘 Breathing Exercise"):
        st.markdown("""
        - **Box Breathing**: Inhale 4s → Hold 4s → Exhale 4s → Hold 4s.
        - Do this for 2–3 minutes to calm your body.
        - [Try it here](https://www.youtube.com/watch?v=YFdZXwE6fRE)
        """)

# Main chatbot function
def chatbot():
    st.title("🧠 Therabot – Your Mental Health Companion")

    # Session state init
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""

    # Input
    user_input = st.text_input("You:", key="user_input")

    # Handle user message
    if user_input:
        st.session_state.chat_history.append(("You", user_input))

        # Bot response
        bot_response = generate_response(user_input)
        st.session_state.chat_history.append(("Therabot", bot_response))
        st.session_state.user_input = ""

    # Chat display
    st.write("### 💬 Conversation")
    for sender, message in st.session_state.chat_history:
        st.markdown(f"**{sender}:** {message}")

    # Extra support sections
    st.divider()
    show_coping_strategies()
    show_relaxation_exercises()

    # Reset button
    if st.button("🗑️ Reset Conversation"):
        st.session_state.chat_history = []
