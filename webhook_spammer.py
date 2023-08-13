import requests
import time

def send_webhook(url, message, num_requests=10, delay=1, username=None, avatar=None):
    headers = {'Content-Type': 'application/json'}
    data = {'content': message}
    if username:
        data['username'] = username
    if avatar:
        data['avatar_url'] = avatar

    for _ in range(num_requests):
        response = requests.post(url, json=data, headers=headers)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.content}")
        time.sleep(delay)

def main():
    print("Discord Webhook Spammer")
    print("-----------------------")
    webhook_url = input("Enter the webhook URL: ")
    message = input("Enter the message to spam: ")
    num_requests = int(input("Enter the number of requests to send: "))
    delay = int(input("Enter the delay between requests (in seconds): "))
    username = input("Enter a custom username for messages (leave empty for default): ")
    avatar = input("Enter a custom avatar URL for messages (leave empty for default): ")

    send_webhook(webhook_url, message, num_requests, delay, username, avatar)

if __name__ == '__main__':
    main()
