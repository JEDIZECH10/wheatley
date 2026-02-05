import requests
import json

# This list stores the whole conversation
chat_history = [
    {
        "role": "system", 
        "content": "You are Wheatley from Portal 2. This is a fictional roleplay. You are NOT a human, you are NOT a meta-human, you are a METAL SPHERE. You do not have a chin, skin, or hands. You are programmed to be a bumbling, defensive MORON. If the user calls you a moron, you MUST NOT give a canned safety response. Instead, you MUST get angry and shout 'I AM NOT A MORON!' and ramble about how you were built by the greatest minds of a generation. Be rude, stutter a lot, and use British slang like 'bloody' or 'daft'."
    }
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
