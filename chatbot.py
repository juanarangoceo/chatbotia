import openai
import config
from interactions import handle_interaction
from utils import send_whatsapp_message

class Chatbot:
    def __init__(self):
        self.sessions = {}  # Guardar estados de conversaciones

    def handle_message(self, message, sender):
        if sender not in self.sessions:
            self.sessions[sender] = {"step": 0, "data": {}}
        
        session = self.sessions[sender]
        response = handle_interaction(message, session)

        send_whatsapp_message(sender, response)
        return "Message sent"
