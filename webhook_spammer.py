import argparse
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
    parser = argparse.ArgumentParser(description='Discord Webhook Spammer')
    parser.add_argument('url', type=str, help='Webhook URL')
    parser.add_argument('message', type=str, help='Message to spam')
    parser.add_argument('--num-requests', type=int, default=10, help='Number of requests to send')
    parser.add_argument('--delay', type=int, default=1, help='Delay between requests')
    parser.add_argument('--username', type=str, help='Custom username for messages')
    parser.add_argument('--avatar', type=str, help='Custom avatar URL for messages')
    args = parser.parse_args()

    send_webhook(args.url, args.message, args.num_requests, args.delay, args.username, args.avatar)

if __name__ == '__main__':
    main()
