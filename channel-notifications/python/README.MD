# Chanel Notifications Python

A bot that will send messages to a channel. It can be configured to send messages every time.
On this example we send a dog every 30 seconds to a telegram channel or group we define. The bot must be a member of the channel or group

```shell
# Run with docker:
## build image
docker build -t telegram-bot .
## run
docker run -d --name tg-bot -e BOT_TOKEN="<BOT_TOKEN>" -e CHAT_ID="<CHAT_ID>"
```