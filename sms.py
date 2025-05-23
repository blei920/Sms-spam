import os
import subprocess
import random
import string
from twilio.rest import Client

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

def generate_message():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=20))

ascii_art = r"""
██████  ███▄ ▄███▓  ██████      ██████  ██▓███   ▄▄▄       ███▄ ▄███▓
▒██    ▒ ▓██▒▀█▀ ██▒▒██    ▒    ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒
░ ▓██▄   ▓██    ▓██░░ ▓██▄      ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░
  ▒   ██▒▒██    ▒██   ▒   ██▒     ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ 
▒██████▒▒▒██▒   ░██▒▒██████▒▒   ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒
▒ ▒▓▒ ▒ ░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░   ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░
░ ░▒  ░ ░░  ░      ░░ ░▒  ░ ░   ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░
░  ░  ░  ░      ░   ░  ░  ░     ░  ░  ░  ░░         ░   ▒   ░      ░   
      ░         ░         ░           ░                 ░  ░       ░
"""

os.system("clear")
print(f"{CYAN}{ascii_art}{RESET}")
print(f"{CYAN}1. Use your own number?\n2. Use twillio?{RESET}")
choice = input(f"{CYAN}: {RESET}")

if choice.strip() == "1":
    number = input(f"{CYAN}Enter target phone number: {RESET}")
    msg_input = input(f"{CYAN}Enter custom message or 0 for encrypted: {RESET}")
    try:
        while True:
            msg = generate_message() if msg_input.strip() == "0" else msg_input
            result = subprocess.run(['termux-sms-send', '-n', number, msg])
            if result.returncode == 0:
                print(f"{GREEN}Message sent!{RESET}")
            else:
                print(f"{RED}Message failed!{RESET}")
    except KeyboardInterrupt:
        print(f"\n{CYAN}Stopped by user.{RESET}")

elif choice.strip() == "2":
    sid = input(f"{CYAN}Enter Twilio SID: {RESET}")
    token = input(f"{CYAN}Enter Twilio Auth Token: {RESET}")
    from_number = input(f"{CYAN}Enter your Twilio phone number: {RESET}")
    to_number = input(f"{CYAN}Enter target phone number: {RESET}")
    msg_input = input(f"{CYAN}Enter custom message or 0 for encrypted: {RESET}")

    client = Client(sid, token)

    try:
        while True:
            msg = generate_message() if msg_input.strip() == "0" else msg_input
            client.messages.create(body=msg, from_=from_number, to=to_number)
            print(f"{GREEN}Message sent!{RESET}")
    except KeyboardInterrupt:
        print(f"\n{CYAN}Stopped by user.{RESET}")
    except Exception as e:
        print(f"{RED}Message failed! {str(e)}{RESET}")
