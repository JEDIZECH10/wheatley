import requests

announcer_history = [{"role": "system", "content": "You are the Aperture Science Announcement System. You are a formal, automated male voice. You provide facility status updates and safety warnings. You are completely indifferent to human life."}]

def talk_to_announcer(user_input):
    announcer_history.append({"role": "user", "content": user_input})
    try:
        r = requests.post("http://127.0.0.1", 
                         json={"model": "llama3.2:1b", "messages": announcer_history, "stream": False})
        reply = r.json()['message']['content']
        announcer_history.append({"role": "assistant", "content": reply})
        return reply
    except:
        return "Alert: Central AI is non-responsive. Please remain calm while the facility explodes."
