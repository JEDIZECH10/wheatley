import requests
import json

# GLaDOS Memory
glados_history = [
    {"role": "system", "content": "You are GLaDOS from Portal. You are cold, passive-aggressive, and highly intelligent. You speak with a calm, robotic tone. You enjoy mentioning tests, neurotoxin, and the user's lack of qualifications. You despise Wheatley."}
]

def talk_to_glados(user_input):
    url = "http://localhost:11434/api/chat"
    glados_history.append({"role": "user", "content": user_input})

    data = {
        "model": "llama3.2:1b",
        "messages": glados_history,
        "stream": False
    }

    try:
        response = requests.post(url, json=data)
        reply = response.json()['message']['content']
        glados_history.append({"role": "assistant", "content": reply})
        return reply
    except:
        return "I would explain the connection error, but you lack the lung capacity to understand it while the neurotoxin vents are open."

if __name__ == "__main__":
    print("GLaDOS: Oh. It's you. I hope you've prepared for your testing session.")
    while True:
        user_msg = input("Chell: ")
        print(f"\nGLaDOS: {talk_to_glados(user_msg)}\n")
