from flask import Flask, request
import requests
import os

app = Flask(__name__)

PHONE_ID = "1448000225056593"
ACCESS_TOKEN = os.environ.get("TOKEN", "")
VERIFY_TOKEN = "elite123"

def send_whatsapp(to, text):
    url = f"https://graph.facebook.com/v20.0/{PHONE_ID}/messages"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}", "Content-Type": "application/json"}
    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }
    requests.post(url, headers=headers, json=data)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Token galat hai"
    
    try:
        entry = request.json['entry'][0]['changes'][0]['value']
        if 'messages' in entry:
            msg = entry['messages'][0]
            from_num = msg['from']
            
            reply_text = """👑 *ELITE FF SERVICES* 👑

🔥 *FREE FIRE LIKES & TOPUP* 🔥

💰 *UPI:* 9996093453@fam
📸 *Insta:* @mohit_ror_011

*RATE LIST:*
1K Likes = Rs 30
5K Likes = Rs 130
10K Likes = Rs 250

*UID Topup Available*

Payment ka screenshot bhejo, 5 min me done kar dunga! 🚀"""
            
            send_whatsapp(from_num, reply_text)
    except Exception as e:
        print(e)
    
    return "ok", 200

@app.route("/")
def home():
    return "ELITE FF BOT IS LIVE - MOHIT ROR"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
