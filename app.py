from flask import Flask, request
from chatbot import Chatbot

app = Flask(__name__)
chatbot = Chatbot()

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").strip()
    sender = request.values.get("From", "")
    response = chatbot.handle_message(incoming_msg, sender)
    return response

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
