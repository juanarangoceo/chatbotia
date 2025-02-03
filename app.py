from flask import Flask, request
from chatbot import Chatbot
import config

app = Flask(__name__)

chatbot = Chatbot()

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").strip()
    sender = request.values.get("From", "")
    response = chatbot.handle_message(incoming_msg, sender)
    return response

if __name__ == "__main__":
    app.run(debug=True)
