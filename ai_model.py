import json
import os
from textblob import TextBlob
from dotenv import load_dotenv
import openai

# Load .env API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load spiritual wisdom data
def load_wisdom():
    with open("knowledge_base/spiritual_wisdom.json", "r", encoding="utf-8") as f:
        return json.load(f)

wisdom_data = load_wisdom()

# Detect emotion from user input
def detect_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.3:
        return "positive"
    elif polarity < -0.3:
        return "negative"
    else:
        return "neutral"

# Suggest spiritual topic based on keywords
def get_topic_from_text(text):
    keywords = {
        "peace": "inner_peace",
        "calm": "inner_peace",
        "angry": "forgiveness",
        "hurt": "forgiveness",
        "thank": "gratitude",
        "grateful": "gratitude",
        "fear": "fear",
        "love": "love",
        "compassion": "compassion",
        "sad": "suffering",
        "pain": "suffering",
        "ego": "ego",
        "truth": "truth",
        "lost": "purpose",
        "why": "purpose",
        "anxious": "mindfulness",
        "present": "mindfulness",
        "change": "letting_go",
        "control": "letting_go"
    }

    for word in text.lower().split():
        if word in keywords:
            return keywords[word]
    return "inner_peace"  # default

# Get spiritual response from knowledge base
def get_spiritual_reply(topic):
    if topic in wisdom_data:
        quotes = wisdom_data[topic]
        selected_quote = list(quotes.values())[0]
        return f"Here is some wisdom on '{topic.replace('_', ' ')}':\n💬 \"{selected_quote}\""
    else:
        return None

# Optionally generate from OpenAI if topic not found
def get_gpt_reply(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a wise spiritual assistant who gives compassionate, interfaith advice using quotes and calming suggestions."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Sorry, I couldn't connect to the wisdom source right now."

# MAIN RESPONSE FUNCTION
def generate_response(user_input):
    emotion = detect_emotion(user_input)
    topic = get_topic_from_text(user_input)

    spiritual_message = get_spiritual_reply(topic)
    
    if spiritual_message:
        return f"🌟 Emotion detected: *{emotion}*\n{spiritual_message}"
    else:
        return get_gpt_reply(user_input)
