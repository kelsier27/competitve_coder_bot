from bot import app

import json
import requests
from flask import request


@app.route("/newMessage", methods=['POST', 'GET'])
def new_message_handler():
    update_json = request.get_json()

    chat_id = update_json["message"]["chat"]["id"]
    payload = {
        "chat_id": chat_id,
        "text": "Hello from the Coder Bot, " + update_json["message"]["chat"]["username"]
                + "This is in response to your message"
    }

    print("Replying with standard response to user with chat_id ", chat_id)
    resp = requests.post(config["bot_base_url"] + config["bot_access_token"] + "/sendMessage", payload)
    print(resp)
    return "Request received"


@app.route("/")
def hello():
    return "Working so far"
