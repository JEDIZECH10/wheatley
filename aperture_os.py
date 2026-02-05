import os
import subprocess
import requests
# These import your other files in the same folder
from wheatley import talk_to_wheatley
from glados import talk_to_glados

def run_terminal():
    # Attempt to wake up Ollama if it's not already running
    os.system("/usr/local/bin/ollama serve > ollama.log 2>&1 &")
    
    # Character Setup
    core = "WHEATLEY"
    color = "\033[94m" # Blue
    
    os.system('clear')
    print(f"{color}APERTURE SCIENCE MULTI-CORE TERMINAL [Version 2.0.4]\033[0m")
    print("Type 'help' for commands, '/swap' to change Cores, or 'exit' to quit.")
    print("-" * 60)

    while True:
        try:
            prompt = f"root@APERTURE:/ {core}> "
            user_input = input(prompt).strip()

            if not user_input: 
                continue
            if user_input.lower() == "exit": 
                print("Shutting down... Goodbye.")
                break
            
            # Special Commands
            if user_input.lower() == "help":
                print("\nSYSTEM COMMANDS: ls, pwd, clear, whoami, /swap")
                print("AI INTERACTION: Just type anything else to talk.\n")
                continue
            
            if user_input.lower() == "/swap":
                core = "GLADOS" if core == "WHEATLEY" else "WHEATLEY"
                color = "\033[93m" if core == "GLADOS" else "\033[94m"
                print(f"\n{color}[!] CORE SWAP: {core} IS NOW IN CONTROL\033[0m\n")
                continue

            # Check for standard Linux commands
            if user_input.split()[0] in ['ls', 'pwd', 'clear', 'whoami', 'cat']:
                result = subprocess.run(user_input, shell=True, capture_output=True, text=True)
                print(result.stdout)
                if result.stderr: print(f"ERROR: {result.stderr}")
                continue

            # If not a command, it's a message for the AI
            if core == "WHEATLEY":
                reply = talk_to_wheatley(user_input)
            else:
                reply = talk_to_glados(user_input)
            
            print(f"\n{color}{core}: {reply}\033[0m\n")

        except KeyboardInterrupt:
            print("\nManual override detected. Exiting...")
            break
        except Exception as e:
            print(f"\n[!] CORE ERROR: {e}\n")

if __name__ == "__main__":
    run_terminal()
