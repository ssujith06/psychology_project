import random

# Define chatbot responses manually
responses = {
    "hello": ["Hey there! 😊", "Hi! How can I help you today?", "Hello! Hope you're doing great!"],
    "how are you": ["I'm just a bot, but I'm feeling awesome! 🤖", "I'm good! How about you?", "Doing great!"],
    "anxious": ["It's okay to feel this way. Try deep breathing. Here’s a helpful link: https://www.calm.com/", 
                "You’re not alone. Maybe some music will help? 🎵"],
    "depression": ["I'm here for you. Talking to a friend might help! 💙", 
                   "You are valuable. Maybe this can help: https://www.betterhelp.com/"],
    "stress": ["Take a deep breath. Inhale... Exhale... 😌", "Want a joke to relax? Type 'joke'!"],
    "joke": ["Why don't skeletons fight each other? Because they don't have the guts! 😂", 
             "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾"],
    "bye": ["Goodbye! Stay happy! 😊", "See you later! Take care!", "Bye! Have a great day!"],
}

def get_response(user_input):
    user_input = user_input.lower()
    
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return "I'm not sure about that, but I’m here to chat! 😊 Try asking about stress, anxiety, or depression."

# Test the chatbot
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! 👋")
            break
        print("Chatbot:", get_response(user_input))
