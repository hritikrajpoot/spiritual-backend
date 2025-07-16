import random
import json
import os

# Load spiritual wisdom quotes
def load_wisdom():
    path = os.path.join("knowledge_base", "spiritual_wisdom.json")
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

wisdom_data = load_wisdom()

# Define emotion categories with sample keywords
emotion_keywords = {
    "sad": ["lost", "empty", "alone", "tired", "hopeless", "cry", "meaningless", "broken"],
    "anxious": ["nervous", "worried", "anxious", "overthinking", "stressed", "panic"],
    "angry": ["angry", "mad", "furious", "frustrated", "annoyed"],
    "happy": ["joyful", "happy", "grateful", "excited", "blessed"],
    "confused": ["confused", "unsure", "unclear", "no direction"],
    "motivated": ["driven", "hopeful", "motivated", "ready", "ambitious"],
    "lonely": ["lonely", "no one", "abandoned", "isolated", "ignored"],
    "spiritual": ["soul", "spiritual", "consciousness", "inner peace", "divine", "enlightened"]
}

# Emotion-based response templates
emotion_responses = {
    "sad": [
        "I feel your pain. Sometimes, allowing yourself to feel is the path to healing.",
        "Even the darkest nights end. Here's something from the Gita: 'In grief, remain steady like a rock.'"
    ],
    "anxious": [
        "Breathe gently. You are safe in this moment. Would you like a calming practice?",
        "Let go of what you can't control. You are doing your best — and that's enough."
    ],
    "angry": [
        "Anger is valid, but you don't have to hold onto it. Let's transform this fire into clarity.",
        "You are heard. Would you like to explore what's beneath the anger?"
    ],
    "happy": [
        "That’s beautiful! Cherish this energy and pass it on.",
        "Let your joy be a light to others. 😊"
    ],
    "confused": [
        "It’s okay not to have it all figured out. Let’s walk through it together.",
        "When you're unsure, listen to your inner stillness — that's where clarity lives."
    ],
    "motivated": [
        "You’re on the right path. What would you like to create today?",
        "Your light is strong. Let’s channel it toward purpose."
    ],
    "lonely": [
        "You are not alone. I’m here with you. Would you like some spiritual companionship?",
        "Your presence matters. Let’s find warmth in this moment together."
    ],
    "spiritual": [
        "The soul always seeks truth. Let me offer you a verse from ancient wisdom.",
        "Let’s expand your awareness. Which path calls to you — peace, growth, or healing?"
    ]
}

# Fallback wisdom response
def get_random_wisdom():
    return random.choice(wisdom_data)["wisdom"]

# Detect emotion from input
def detect_emotion(user_input):
    user_input = user_input.lower()
    for emotion, keywords in emotion_keywords.items():
        for word in keywords:
            if word in user_input:
                return emotion
    return None

# Generate AI response
def generate_response(user_input):
    emotion = detect_emotion(user_input)
    
    if emotion:
        response = random.choice(emotion_responses[emotion])
        return f"💬 ({emotion.upper()} detected): {response}"
    else:
        # Default fallback to wisdom
        return f"🌟 Here's something that may help:\n“{get_random_wisdom()}”"

# For local test
if __name__ == "__main__":
    test_inputs = [
        "I feel lost and broken",
        "I'm so excited for my future!",
        "Nobody listens to me",
        "I’m confused about my life direction",
        "I’m having an anxiety attack",
        "My heart feels empty"
    ]
    for text in test_inputs:
        print(f"User: {text}")
        print("AI:", generate_response(text))
        print("------")
