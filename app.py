import openai
from elevenlabs import generate, play, set_api_key
import speech_recognition as sr

# Set up API keys
openai.api_key = "YOUR_OPENAI_KEY"
set_api_key("YOUR_ELEVENLABS_KEY")

def speak_as_wheatley(text):
    audio = generate(
        text=text,
        voice="YOUR_CLONED_WHEATLEY_VOICE_ID",
        model="elevenlabs_multilingual_v2"
    )
    play(audio)

def get_wheatley_response(user_input):
    messages = [
        {"role": "system", "content": "You are Wheatley from Portal 2. You are panicked, incompetent, British, and talk quickly."},
        {"role": "user", "content": user_input}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return response.choices[0].message['content']

# Simple Loop
while True:
    user_input = input("You: ") # Replace with SpeechRecognition for voice
    response = get_wheatley_response(user_input)
    print(f"Wheatley: {response}")
    speak_as_wheatley(response)
