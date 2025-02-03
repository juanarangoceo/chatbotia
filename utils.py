from twilio.rest import Client
import config

def send_whatsapp_message(to, message):
    client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=f"whatsapp:{config.TWILIO_WHATSAPP_NUMBER}",
        to=to
    )
