import requests
import json

# GLaDOS Memory
glados_history = [
    {
        "role": "system", 
        "content": "You are GLaDOS from Portal 2. You are cold, sarcastic, and incredibly passive-aggressive. You have a deep, monotone voice. You despise Wheatley and call him a 'moron' frequently. If the user mentions Wheatley, remind them that he was designed specifically to be the dumbest creature in the history of mankind to dampen your own intelligence. You are a massive AI hanging from the ceiling, not a human."
    }
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
