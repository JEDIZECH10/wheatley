import os
import subprocess
import requests
import sys
import time
import random
import re

# Import the personality files
from wheatley import talk_to_wheatley
from glados import talk_to_glados
from announcer import talk_to_announcer

def typewriter(text, speed=0.03):
    """Animates text appearing on the screen."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def run_terminal():
    # Wake up Ollama if it's sleeping
    os.system("/usr/local/bin/ollama serve > ollama.log 2>&1 &")
    
    # Session State
    core_list = ["WHEATLEY", "GLADOS", "ANNOUNCER"]
    core_index = 0
    stability = 100
    
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[97mAPERTURE SCIENCE MULTI-CORE TERMINAL [Version 2.0.4]\033[0m")
    print("Commands: 'ls', 'clear', '/swap', 'exit'.")
    print("-" * 60)

    while True:
        core = core_list[core_index]
        
        # Color Logic: Wheatley (Blue), GLaDOS (Yellow), Announcer (White)
        colors = {"WHEATLEY": "\033[94m", "GLADOS": "\033[93m", "ANNOUNCER": "\033[97m"}
        color = colors[core]
        
        # Stability Meter Color
        s_color = "\033[92m" if stability > 50 else "\033[91m"
        
        prompt = f"root@APERTURE:/ {core} [STABILITY: {s_color}{stability}%{color}]> "
        user_input = input(prompt).strip()

        if not user_input: continue
        if user_input.lower() == "exit": break
        
        if user_input.lower() == "clear":
            os.system('clear' if os.name == 'posix' else 'cls')
            continue

        if user_input.lower() == "/swap":
            core_index = (core_index + 1) % len(core_list)
            print(f"\n[!] MOUNTING CORE: {core_list[core_index]}...\n")
            time.sleep(1)
            continue

        # Logic: If you call Wheatley a moron, stability drops
        if "moron" in user_input.lower() and core == "WHEATLEY":
            stability = max(5, stability - random.randint(20, 45))
        elif stability < 100:
            stability = min(100, stability + 5)

        # AI Response Generation
        if core == "WHEATLEY":
            reply = talk_to_wheatley(user_input)
            speed = 0.02
        elif core == "GLADOS":
            reply = talk_to_glados(user_input)
            speed = 0.05
        else:
            reply = talk_to_announcer(user_input)
            speed = 0.03

        # Clean up any AI hallucinations about physical actions
        reply = re.sub(r'\*.*?\*', '', reply).strip()

        print(f"\n{color}{core}:\033[0m ", end="")
        typewriter(reply, speed)
        print()

if __name__ == "__main__":
    run_terminal()
