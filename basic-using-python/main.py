import requests
import time

TOKEN = '<BOT_TOKEN>'
URL = f"https://api.telegram.org/bot{TOKEN}/"

def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += f"&offset={offset}"
    response = requests.get(url)
    return response.json()

def send_message(chat_id, text):
    url = URL + f"sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)

def handle_commands(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat_id = update["message"]["chat"]["id"]
            if text.startswith("/"):
                # Split command and arguments
                parts = text.split(" ", 1)
                command = parts[0].lower()
                args = parts[1] if len(parts) > 1 else ""

                if command == "/start":
                    send_message(chat_id, "Welcome to the bot! Use /echo [message] to echo your message.")
                elif command == "/echo":
                    if args:
                        send_message(chat_id, f"Echo: {args}")
                    else:
                        send_message(chat_id, "Please provide a message to echo. Usage: /echo [message]")
            else:
                send_message(chat_id, "I'm not sure what you're asking for. Try /start or /echo.")
        except Exception as e:
            print(f"Error handling update: {e}")

def handle_updates(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat_id = update["message"]["chat"]["id"]
            send_message(chat_id, f"Echo: {text}")
        except Exception as e:
            print(f"Error handling update: {e}")

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if updates["result"]:
            last_update_id = updates["result"][-1]["update_id"] + 1
            handle_commands(updates)
        time.sleep(1)

if __name__ == '__main__':
    main()