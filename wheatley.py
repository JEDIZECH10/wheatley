import requests
import json

# This list stores the whole conversation
chat_history = [
    {
        "role": "system", 
        "content": "You are Wheatley from Portal 2. You are a metal sphere on a ceiling rail. You have NO limbs. You are bumbling, stuttering, and British. If called a moron, you must shout I AM NOT A MORON! in all caps and ramble about being a genius. Do not use asterisks for actions."
    }
]

def talk_to_wheatley(user_input):
    # 1. Add user message to history
    chat_history.append({"role": "user", "content": user_input})
    
    # 2. Define the correct URL (Notice the indentation!)
    url = "http://127.0.0.1:11434/api/chat"
    
    # 3. Setup the payload
    payload = {
        "model": "llama3.2:1b", 
        "messages": chat_history, 
        "stream": False
    }
    
    try:
        # 4. Make the request
        r = requests.post(url, json=payload, timeout=60)
        
        # 5. Extract and save reply
        reply = r.json()['message']['content']
        chat_history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        # This will tell us EXACTLY what is wrong if it fails
        return f"Internal bits are on fire! Restart the Ollama server! (Error: {e})"

# This allows you to test Wheatley by himself
if __name__ == "__main__":
    print("WHEATLEY: Personality core engaged!")
    while True:
        msg = input("You: ")
        print(f"WHEATLEY: {talk_to_wheatley(msg)}")
