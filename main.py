import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "توصية" in incoming_msg:
        msg.body("توصية ذهب تجريبية: شراء من 3215، الهدف 3225، وقف الخسارة 3205.")
    else:
        msg.body("مرحباً! أرسل كلمة 'توصية' للحصول على توصية ذهب.")

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
