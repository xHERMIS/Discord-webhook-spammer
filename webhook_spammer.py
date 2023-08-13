import requests
import time
import warnings
import os
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

def send_webhook(url, message, num_requests=10, delay_ms=1000, username=None, avatar=None):
    headers = {'Content-Type': 'application/json'}
    data = {'content': message}
    if username:
        data['username'] = username
    if avatar:
        data['avatar_url'] = avatar

    # Filter out RequestsDependencyWarning
    warnings.filterwarnings("ignore", category=requests.RequestsDependencyWarning)

    for i in range(1, num_requests + 1):
        response = requests.post(url, json=data, headers=headers)
        print(f"{Fore.YELLOW}Request {i}:")
        print(f"Status Code: {Fore.CYAN}{response.status_code}")
        print(f"Response Content: {Fore.GREEN}{response.content}\n")
        time.sleep(delay_ms / 1000)  # Convert delay_ms to seconds

def main():
    print(f"{Fore.MAGENTA}Discord Webhook Spammer")
    print(f"{Fore.MAGENTA}-----------------------")
    print(COPYRIGHT_NOTICE)  # Display copyright notice
    print(f"{Fore.YELLOW}Developed by {Fore.MAGENTA}HERMIS <3{Fore.RESET}")  # Display your Discord username
    webhook_url = input("Enter the webhook URL: ")
    message = input("Enter the message to spam: ")
    num_requests = int(input("Enter the number of requests to send: "))
    delay_ms = int(input("Enter the delay between requests (in milliseconds): "))
    username = input("Enter a custom username for messages (leave empty for default): ")
    avatar = input("Enter a custom avatar URL for messages (leave empty for default): ")

    send_webhook(webhook_url, message, num_requests, delay_ms, username, avatar)

if __name__ == '__main__':
    main()
