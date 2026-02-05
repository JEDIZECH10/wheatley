import requests
import json

# This list stores the whole conversation
chat_history = [
    {"role": "system", "content": "You are Wheatley from Portal 2. You are a 'Intelligence Dampening Sphere'. You are British, stutter, and are incredibly over-confident but wrong. You ramble. Never admit you are a moron."}
]

def talk_to_wheatley(user_input):
    url = "http://localhost:11434/api/chat" # Changed to /chat for history support
    
    # Add your new message to the memory
    chat_history.append({"role": "user", "content": user_input})

    data = {
        "model": "llama3.2:1b",
        "messages": chat_history,
        "stream": False
    }

    try:
        response = requests.post(url, json=data)
        wheatley_reply = response.json()['message']['content']
        
        # Add Wheatley's reply to memory so he remembers what he said
        chat_history.append({"role": "assistant", "content": wheatley_reply})
        
        return wheatley_reply
    except Exception as e:
        return f"Oh, brilliant. My internal bits are on fire. (Error: {e})"

if __name__ == "__main__":
    print("WHEATLEY: Personality core engaged! I'm speaking to you from a cloud! A literal cloud! Don't look down.")
    while True:
        user_msg = input("You: ")
        if user_msg.lower() in ["exit", "quit"]: break
        
        reply = talk_to_wheatley(user_msg)
        print(f"\nWHEATLEY: {reply}\n")
