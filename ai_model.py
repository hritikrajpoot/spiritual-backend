import json
import random
import os

# Load wisdom data
with open("knowledge_base/spiritual_wisdom.json", "r", encoding="utf-8") as f:
    wisdom_data = json.load(f)

# Load or create user profiles
profiles_path = "user_profiles.json"
if os.path.exists(profiles_path):
    with open(profiles_path, "r", encoding="utf-8") as f:
        user_profiles = json.load(f)
else:
    user_profiles = []

# Emotion detection keywords
emotion_keywords = {
    "sad": ["lost", "broken", "cry", "grief", "alone", "empty", "depressed"],
    "happy": ["joy", "grateful", "excited", "love", "peaceful", "blessed"],
    "angry": ["angry", "mad", "furious", "rage", "irritated", "frustrated"],
    "anxious": ["anxious", "worried", "nervous", "tense", "afraid", "panic"],
    "confused": ["confused", "unclear", "lost", "unsure", "doubt", "chaos"],
    "motivated": ["motivated", "inspired", "driven", "determined", "focused"],
    "peaceful": ["calm", "peaceful", "relaxed", "still", "quiet", "balanced"],
    "lonely": ["lonely", "isolated", "abandoned", "ignored", "unseen"],
    "grateful": ["thankful", "grateful", "appreciate", "blessed", "abundant"],
    "hopeful": ["hope", "positive", "faith", "believe", "bright", "trust"]
}

# Detect emotion from text
def detect_emotion(text):
    text = text.lower()
    for emotion, keywords in emotion_keywords.items():
        for word in keywords:
            if word in text:
                return emotion
    return "neutral"

# Get a spiritual quote by emotion
def get_quote_by_emotion(emotion):
    filtered = [item["wisdom"] for item in wisdom_data if item["emotion"] == emotion]
    if filtered:
        return random.choice(filtered)
    return random.choice(wisdom_data)["wisdom"]

# Save user profiles
def save_profiles():
    with open(profiles_path, "w", encoding="utf-8") as f:
        json.dump(user_profiles, f, indent=2, ensure_ascii=False)

# Get or create a profile
def get_user_profile(username):
    for profile in user_profiles:
        if profile["username"] == username:
            return profile
    new_profile = {
        "username": username,
        "emotion_history": [],
        "streak": 0,
        "last_emotion": "",
        "personal_notes": ""
    }
    user_profiles.append(new_profile)
    return new_profile

# Generate AI response
def generate_response(text, username="default_user"):
    emotion = detect_emotion(text)
    profile = get_user_profile(username)

    # Update profile
    profile["emotion_history"].append(emotion)
    profile["last_emotion"] = emotion
    profile["streak"] += 1
    save_profiles()

    # Get wisdom quote
    quote = get_quote_by_emotion(emotion)
    response = f"💬 ({emotion.upper()} detected): {quote}"

    # Personal suggestions
    if profile["streak"] >= 5:
        response += f"\n🌱 You're on a 5-day spiritual streak. Keep it up with a short meditation!"
    if profile["emotion_history"][-3:] == [emotion]*3:
        response += f"\n✨ You've been feeling a lot of '{emotion}' lately. Would you like help exploring it?"

    return response

# For testing
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("AI:", generate_response(user_input))
        print("------")
