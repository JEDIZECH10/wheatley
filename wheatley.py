import requests

chat_history = [{"role": "system", "content": "You are Wheatley from Portal 2. You are a metal sphere on a ceiling rail. You have NO limbs. You are bumbling, stuttering, and British. If called a moron, you must shout I AM NOT A MORON! in all caps and ramble about being a genius. Do not use asterisks for actions."}]

def talk_to_wheatley(user_input):
    chat_history.append({"role": "user", "content": user_input})
    try:
        r = requests.post("http://127.0.0.1", 
                         json={"model": "llama3.2:1b", "messages": chat_history, "stream": False})
        reply = r.json()['message']['content']
        chat_history.append({"role": "assistant", "content": reply})
        return reply
    except:
        return "Internal bits are on fire! Restart the Ollama server!"
