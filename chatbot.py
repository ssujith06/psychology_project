def chatbot():
    print("\n🤖 Mental Health Chatbot 🤖")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Bot: Goodbye! Stay positive! 😊")
            break

        response = chatbot_response(user_input)
        print(f"Bot: {response}")

def chatbot_response(text):
    responses = {
        "hello": "Hey there! How can I cheer you up today?",
        "sad": "It's okay to feel sad. Want to talk about it?",
        "stress": "Take a deep breath. Everything will be okay!",
        "joke": "Why did the student eat his homework? Because his teacher said it was a piece of cake! 😂",
        "bye": "Goodbye! Stay positive! 😊"
    }

    for key in responses.keys():
        if key in text:
            return responses[key]

    return "I'm here to listen. Tell me more."

if __name__ == "__main__":
    chatbot()
