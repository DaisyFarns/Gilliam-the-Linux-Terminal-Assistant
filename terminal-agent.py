#!/usr/bin/env python3
import os
import sys
import subprocess
import readline
from datetime import datetime

BANNER = r"""
╔══════════════════════════════════╗
║  🧠 TERMINAL AGENT: ONLINE       ║
╚══════════════════════════════════╝
"""

HELP_TEXT = '''
COMMAND MODES:
• Any terminal command → Executes normally.
• Question (contains '?' or starts with what/how/why) → Explains using man pages or built-in help.
• 'exit' or 'quit' → Ends the session.
'''

def is_question(text):
    lowered = text.lower()
    return '?' in text or lowered.startswith(('what', 'how', 'why', 'help', 'explain'))

def get_manual_info(cmd):
    try:
        man_output = subprocess.check_output(['man', cmd], stderr=subprocess.DEVNULL).decode()
        print("\n📖 Showing manual info (first 20 lines):\n")
        print("\n".join(man_output.splitlines()[:20]))
    except Exception:
        print("❌ No manual entry found.")

def execute_command(cmd):
    try:
        subprocess.run(cmd, shell=True)
    except Exception as e:
        print(f"🔥 Command failed: {e}")

def load_api_key():
    # TODO: Write this function
    raise NotImplementedError()

def ask_gpt(cmd, api_key):
    # TODO: Write this function
    raise NotImplementedError()

def main():
    print(BANNER)
    print("Type a command or ask a question. Type 'exit' to quit.")
    print(HELP_TEXT)

    api_key = load_api_key()
    if api_key:
        print("🔑 OpenAI API key loaded: GPT support is ENABLED.")
    else:
        print("⚠️ No OpenAI API key found. GPT support is DISABLED.")

    while True:
        try:
            cmd = input("agent> ").strip()
            if cmd.lower() in ['exit', 'quit']:
                print("👋 Agent signing off.")
                break
            elif not cmd:
                continue
            elif is_question(cmd):
                if api_key:
                    answer = ask_gpt(cmd, api_key)
                    print("🧠 GPT says:\n" + answer)

                    # TODO: Implement system to extract commands
                    # from ChatGPT answer
                else:
                    parts = cmd.strip().split()

                    # It's difficult to extract the name of the program,
                    # but the first element is I think the most likely
                    target = parts[0]
                    
                    get_manual_info(target)
            else:
                execute_command(cmd)
        except KeyboardInterrupt:
            print("\n🛑 Ctrl+C received. Agent shutting down.")
            break

if __name__ == "__main__":
    main()