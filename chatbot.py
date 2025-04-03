import random

responses = {
    "hello": ["Hey there! 👋", "Namaste! 🙏", "Hola! 😃"],
    "how are you": ["I'm an AI, but I feel fantastic! 🚀", "I'm doing as good as a WiFi with full bars! 📶"],
    "joke": ["Why don't scientists trust atoms? Because they make up everything! 😂", 
             "Why was the math book sad? Because it had too many problems! 📖"],
    "outpass": ["Need an outpass? First, convince me with a joke! 😆", 
                "Outpass? Don't forget to return on time! ⏳"],
}

def get_response(user_input):
    user_input = user_input.lower()

    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    
    return "I'm still learning! But I can tell jokes. Type 'joke'! 😃"
