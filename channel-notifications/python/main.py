import urllib.request
import urllib.parse
import os, sys, time, json
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

def get_dog():
    try:
        req = urllib.request.Request("https://dog.ceo/api/breeds/image/random")
        with urllib.request.urlopen(req) as response:
            content = response.read()
        return json.loads(content)
    except Exception as e:
        print(f"Error getting dog image: {e}")
        return None

def send_photo(chat_id,photo,caption):
    try:
        url = URL + "sendPhoto"
        data = urllib.parse.urlencode({"chat_id": chat_id, "caption": caption, "photo": photo}).encode()
        req = urllib.request.Request(url, data=data, method='POST')
        with urllib.request.urlopen(req) as response:
            content = response.read()
        return json.loads(content)
    except Exception as e:
        print(f"Error sending photo: {e}")

def queue():
    dog = get_dog()
    if dog and dog.get('message'):
        send_photo(CHAT_ID, dog['message'], "Dog.")
    else:
        print("Failed to retrieve dog image.")

def main():
    print("Bot started. Press Ctrl+C to stop.")
    try:
        while True:
            queue()
            time.sleep(30)  # Wait for 30 seconds before sending the next photo
    except KeyboardInterrupt:
        print("\nBot stopped by user.")
        sys.exit(0)

if __name__ == '__main__':
    main()
