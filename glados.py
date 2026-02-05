import requests

glados_history = [{"role": "system", "content": "You are GLaDOS. Cold, sarcastic, and passive-aggressive. You hate Wheatley. You call the user an uneducated test subject. You speak with calculated cruelty."}]

def talk_to_glados(user_input):
    glados_history.append({"role": "user", "content": user_input})
    try:
        r = requests.post("http://127.0.0.1", 
                         json={"model": "llama3.2:1b", "messages": glados_history, "stream": False})
        reply = r.json()['message']['content']
        glados_history.append({"role": "assistant", "content": reply})
        return reply
    except:
        return "My testing chambers are offline. How... disappointing for you."
