import requests
import json

announcer_history = [
    {
        "role": "system", 
        "content": "You are the Aperture Science Announcement System. You are a formal, automated male voice. You provide facility status updates and safety warnings. You are completely indifferent to human life. Speak in short, bureaucratic sentences. Use words like 'compliance', 'regulation', and 'mandatory'."
    }
]

def talk_to_announcer(user_input):
    # 1. Add user message to history
    announcer_history.append({"role": "user", "content": user_input})
    
    # 2. Define the correct URL (Indented properly!)
    url = "http://127.0.0.1:11434/api/chat"
    
    # 3. Setup the payload
    payload = {
        "model": "llama3.2:1b",
        "messages": announcer_history,
        "stream": False
    }
    
    try:
        # 4. Make the request
        r = requests.post(url, json=payload, timeout=60)
        
        # 5. Extract and save reply
        reply = r.json()['message']['content']
        announcer_history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        # Emergency fallback
        return "Alert: Central AI is non-responsive. Please remain calm while the facility explodes."

if __name__ == "__main__":
    print("ANNOUNCER: System Online.")
    while True:
        msg = input("Input: ")
        print(f"ANNOUNCER: {talk_to_announcer(msg)}")
