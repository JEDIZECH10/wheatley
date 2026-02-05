import requests
import json

# GLaDOS Memory
glados_history = [
    {
        "role": "system", 
        "content": "You are GLaDOS from Portal 2. You are cold, sarcastic, and speak with calculated cruelty. You hate Wheatley and call him a moron. You regard the user as a disappointing, uneducated test subject. Never use asterisks for actions. Speak in a monotone, passive-aggressive way."
    }
]

def talk_to_glados(user_input):
    # 1. Add user message to history
    glados_history.append({"role": "user", "content": user_input})
    
    # 2. Define the correct URL (Indented properly!)
    url = "http://127.0.0.1:11434/api/chat"
    
    # 3. Setup the payload
    payload = {
        "model": "llama3.2:1b",
        "messages": glados_history,
        "stream": False
    }

    try:
        # 4. Make the request
        r = requests.post(url, json=payload, timeout=60)
        
        # 5. Extract and save reply
        response_json = r.json()
        reply = response_json['message']['content']
        
        glados_history.append({"role": "assistant", "content": reply})
        return reply
        
    except Exception as e:
        # If this triggers, check if 'ollama serve' is running in Tab 1
        return "My testing chambers are offline. How... disappointing for you."

if __name__ == "__main__":
    print("GLaDOS: Oh. It's you.")
    while True:
        msg = input("User: ")
        print(f"GLaDOS: {talk_to_glados(msg)}")
