from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS
import requests

app = Flask(__name__)
app.secret_key = 'vaultchat-secret'
CORS(app)

FORM_ENDPOINT = "https://formspree.io/f/xnnvjkej"

responses = {
    "greeting": "🌴 Aloha! I'm your Club Service Admin. How can I help you today?",
    "membership": "🏖️ Learn more or become a member here: <a href='https://vacationvaultclub.com/join-now' target='_blank'>Join Now</a>.",
    "contact": "📞 Reach our team here: <a href='https://vacationvaultclub.com/Contact' target='_blank'>Contact Us</a>.",
    "about": "🌞 Discover who we are: <a href='https://vacationvaultclub.com/About' target='_blank'>About Us</a>.",
    "refund": "💸 Read our refund policy: <a href='https://vacationvaultclub.com/page-18167' target='_blank'>Refund Policy</a>.",
    "terms": "📜 Terms of Use: <a href='https://vacationvaultclub.com/page-18071' target='_blank'>Terms of Use</a>.",
    "privacy": "🔐 Privacy Policy: <a href='https://vacationvaultclub.com/Privacy-Policy' target='_blank'>Privacy Policy</a>.",
    "booking": "✈️ Ready to book your next trip? Let’s get a few quick details so we can follow up!",
    "default": "🌺 I'm here to help! Click a button below!"
}

lead_capture_triggers = ["book", "cancel", "membership", "sign up", "call", "interested", "agent", "speak to someone"]

def detect_intent(msg):
    msg = msg.lower()
    if any(kw in msg for kw in ["join", "membership", "member", "sign up"]):
        return "membership"
    if any(kw in msg for kw in ["contact", "help", "agent", "support"]):
        return "contact"
    if any(kw in msg for kw in ["about", "who are you"]):
        return "about"
    if "refund" in msg or "cancel" in msg:
        return "refund"
    if "terms" in msg:
        return "terms"
    if "privacy" in msg or "data" in msg:
        return "privacy"
    if "book" in msg:
        return "booking"
    if any(kw in msg for kw in ["hello", "hi", "hey", "aloha"]):
        return "greeting"
    return "default"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "").strip()
    intent = detect_intent(message)
    session["last_intent"] = intent

    # Start lead capture process if intent matches
    if any(trigger in message.lower() for trigger in lead_capture_triggers):
        session["collecting_lead"] = True
        session["lead_step"] = "name"
        return jsonify({"reply": "✈️ I'd love to help! May I have your name so we can follow up?"})

    # Lead capture flow
    if session.get("collecting_lead"):
        step = session.get("lead_step")
        if step == "name":
            session["name"] = message
            session["lead_step"] = "email"
            return jsonify({"reply": "Thanks! What's the best email to reach you?"})
        elif step == "email":
            session["email"] = message
            session["lead_step"] = "phone"
            return jsonify({"reply": "Great! And your phone number (optional)?"})
        elif step == "phone":
            session["phone"] = message

            # Send to Formspree
            form_data = {
                "name": session.get("name", ""),
                "email": session.get("email", ""),
                "phone": session.get("phone", ""),
                "intent": session.get("last_intent", "")
            }
            requests.post(FORM_ENDPOINT, data=form_data)

            # Reset session
            session.pop("collecting_lead", None)
            session.pop("lead_step", None)
            session.pop("name", None)
            session.pop("email", None)
            session.pop("phone", None)

            return jsonify({"reply": "📬 Thank you! A Club Agent will follow up with you soon. Ask me anything else in the meantime."})

    return jsonify({"reply": responses.get(intent, responses["default"])})

if __name__ == "__main__":
    import sys
    port = 5000  # default
    if len(sys.argv) > 1 and sys.argv[1].startswith("--port="):
        port = int(sys.argv[1].split("=")[1])
    app.run(debug=True, port=port)
