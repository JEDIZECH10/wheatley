from wheatley import talk_to_wheatley
from glados import talk_to_glados
import os

def run_terminal():
    # Wake up the brain
    os.system("/usr/local/bin/ollama serve > ollama.log 2>&1 &")
    
    current_core = "WHEATLEY"
    print(f"--- APERTURE SCIENCE TERMINAL ---")
    print(f"SYSTEM: Current Core is {current_core}")
    print("Type '/swap' to change cores or '/exit' to quit.\n")

    while True:
        user_msg = input(f"[{current_core} SESSION] You: ")
        
        if user_msg.lower() == '/exit':
            break
        if user_msg.lower() == '/swap':
            current_core = "GLADOS" if current_core == "WHEATLEY" else "WHEATLEY"
            print(f"\n--- SWITCHING CORES: {current_core} NOW IN CONTROL ---\n")
            continue

        if current_core == "WHEATLEY":
            reply = talk_to_wheatley(user_msg)
        else:
            reply = talk_to_glados(user_msg)
            
        print(f"\n{current_core}: {reply}\n")

if __name__ == "__main__":
    run_terminal()
