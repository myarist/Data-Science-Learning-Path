import json

with open('message.json') as message_json:
  message = json.load(message_json)
print(message)