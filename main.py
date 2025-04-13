import os
from flask import Flask
from twilio.rest import Client

app = Flask(__name__)

@app.route("/")
def home():
    return "M7GOLD Bot is running!"

# Send WhatsApp message on startup
def send_whatsapp_message():
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="whatsapp:+14155238886",
        to="whatsapp:+971556868131",
        body="توصية ذهب تجريبية:
شراء من 3215
الهدف 3225
وقف الخسارة 3205
(تلقائي عند تشغيل البوت)"
    )
    print(f"Message SID: {message.sid}")

if __name__ == "__main__":
    send_whatsapp_message()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
