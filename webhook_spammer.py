import requests
import time
import warnings
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Copyright notice
COPYRIGHT_NOTICE = f"""
{Fore.MAGENTA}
██   ██ ███████ ██████  ███    ███ ██ ███████ 
██   ██ ██      ██   ██ ████  ████ ██ ██      
███████ █████   ██████  ██ ████ ██ ██ ███████ 
██   ██ ██      ██   ██ ██  ██  ██ ██      ██ 
██   ██ ███████ ██   ██ ██      ██ ██ ███████ 
{Fore.RESET}
"""

def send_webhook(url, message, num_requests=10, delay_ms=1000, mention=None, username=None, avatar=None):
    headers = {'Content-Type': 'application/json'}
    data = {'content': message}
    if mention:
        data['content'] += " " + mention
    if username:
        data['username'] = username
    if avatar:
        data['avatar_url'] = avatar

    # Filter out RequestsDependencyWarning
    warnings.filterwarnings("ignore", category=requests.RequestsDependencyWarning)

    for i in range(1, num_requests + 1):
        response = requests.post(url, json=data, headers=headers)
        print(f"{Fore.LIGHTYELLOW_EX}Request {i}:\n")
        print(f"{Fore.CYAN}Status Code: {response.status_code}")
        print(f"{Fore.GREEN}Response Content: {response.content}\n")
        time.sleep(delay_ms / 1000)  # Convert delay_ms to seconds

def main():
    print(f"{Fore.MAGENTA}╔══════════════════════════════════════╗")
    print(f"║{COPYRIGHT_NOTICE:^40}║")
    print(f"║    Developed by {Fore.MAGENTA}HERMIS <3{Fore.RESET}{'':^14}    ║")
    print(f"╚══════════════════════════════════════╝")

    while True:
        choice = input(f"{Fore.LIGHTYELLOW_EX}Do you want to mention {Fore.LIGHTWHITE_EX}everyone{Fore.LIGHTYELLOW_EX} or {Fore.LIGHTWHITE_EX}here{Fore.LIGHTYELLOW_EX}? ").lower()
        if choice == 'everyone':
            mention = '@everyone'
            break
        elif choice == 'here':
            mention = '@here'
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please enter 'everyone' or 'here'.")

    while True:
        webhook_url = input(f"{Fore.LIGHTYELLOW_EX}Enter the webhook URL: ")
        if "discord.com/api/webhooks" in webhook_url:
            break
        else:
            print(f"{Fore.RED}Invalid webhook URL. Please provide a valid Discord webhook URL.")

    while True:
        message = input(f"{Fore.LIGHTYELLOW_EX}Enter the message to spam: ")
        if message.strip():
            break
        else:
            print(f"{Fore.RED}Error: Message cannot be empty. Please provide a message.")

    while True:
        num_requests_input = input(f"{Fore.LIGHTYELLOW_EX}Enter the number of requests to send: ")
        if num_requests_input.isdigit():
            num_requests = int(num_requests_input)
            break
        else:
            print(f"{Fore.RED}Error: Please enter a valid number.")

    while True:
        delay_ms_input = input(f"{Fore.LIGHTYELLOW_EX}Enter the delay between requests (in milliseconds): ")
        if delay_ms_input.isdigit():
            delay_ms = int(delay_ms_input)
            break
        else:
            print(f"{Fore.RED}Error: Please enter a valid number.")

    username = input(f"{Fore.LIGHTYELLOW_EX}Enter a custom username for messages (leave empty for default): ")
    avatar = input(f"{Fore.LIGHTYELLOW_EX}Enter a custom avatar URL for messages (leave empty for default): ")

    send_webhook(webhook_url, message, num_requests, delay_ms, mention, username, avatar)

if __name__ == '__main__':
    main()
