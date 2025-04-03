import nltk
nltk.download('vader_lexicon')  # This is needed for sentiment analysis
import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download sentiment analysis tool
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Define humor-infused mental health responses
responses = {
    "stress": [
        "Stress? No worries! Try breathing exercises. Or scream into a pillow. Either works! 😆",
        "Stress is temporary, but memes are forever! Check this: [Funny Memes](https://www.reddit.com/r/memes/) 🤣",
        "Deep breaths... or just eat a chocolate. Works every time! 🍫"
    ],
    "anxiety": [
        "Anxiety? I get it. Just take things one step at a time. Or dance randomly—it helps! 💃",
        "When life gives you anxiety, make anxiety-ade? 🤷‍♂️ But seriously, this might help: [Anxiety Tips](https://www.verywellmind.com/)",
        "Close your eyes and count sheep. If they start talking, call me. 😂"
    ],
    "depression": [
        "Feeling low? I'm here for you! Also, here's a cat video to cheer you up: [Cute Cats](https://www.youtube.com/results?search_query=cute+cats) 🐱",
        "Depression sucks, but you're not alone! Talk to a friend or check this: [Help](https://www.samhsa.gov)",
        "Need a hug? Sending you a virtual one! 🤗"
    ],
    "joke": [
        "Why don’t skeletons fight each other? They don’t have the guts! 😂",
        "What did one wall say to the other wall? 'I'll meet you at the corner!' 🤣",
        "I told my computer I needed a break… Now it won’t stop sending vacation ads. 😆"
    ],
    "motivation": [
        "You got this! 💪 'Difficult roads often lead to beautiful destinations.'",
        "Remember: Every expert was once a beginner! Keep going. 🚀",
        "If life gives you lemons, make a lemon battery and become famous! ⚡"
    ],
    "default": ["I'm here to chat! Try asking about stress, anxiety, or jokes! 😃"]
}

def get_response(user_input):
    user_input = user_input.lower()

    # Analyze sentiment
    sentiment_score = sia.polarity_scores(user_input)['compound']

    # Determine if user is in distress
    if "depressed" in user_input or sentiment_score < -0.5:
        return random.choice(responses["depression"])
    elif "stress" in user_input:
        return random.choice(responses["stress"])
    elif "anxiety" in user_input:
        return random.choice(responses["anxiety"])
    elif "joke" in user_input or "funny" in user_input:
        return random.choice(responses["joke"])
    elif "motivate" in user_input or "inspire" in user_input:
        return random.choice(responses["motivation"])
    
    return random.choice(responses["default"])
