import requests
import os

# Your Codespace URL from the Ports Tab
URL = "https://your-codespace-url-here-8000.app.github.dev"
current_char = "wheatley"

while True:
    msg = input(f"Send to {current_char.upper()}: ")
    
    if msg == "/swap":
        current_char = "glados" if current_char == "wheatley" else "wheatley"
        print(f"Swapped to {current_char}")
        continue

    # Tell the Codespace which character we are talking to
    r = requests.post(URL, json={"character": current_char, "message": msg})
    response_text = r.json().get("response")
    print(f"Response: {response_text}")

    # Voice Selection logic
    voice = "en-GB-ThomasNeural" if current_char == "wheatley" else "en-US-JennyNeural"
    
    # Generate and play
    os.system(f'edge-tts --voice {voice} --text "{response_text}" --write-media temp.mp3')
    os.system("start temp.mp3")
