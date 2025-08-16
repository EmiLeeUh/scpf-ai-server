from flask import Flask, request, jsonify

# For now, a simple AI-like logic
def ai_response(message):
    # Example: simple keyword responses
    if "hello" in message.lower():
        return "Hello, agent. How can I assist you today?"
    elif "status" in message.lower():
        return "All systems are running normally."
    else:
        return f"(AI) You said: {message}"

app = Flask(__name__)

@app.get("/ping")
def ping():
    return "pong"

@app.post("/npc")
def npc():
    user_msg = request.json.get("message", "")
    reply = ai_response(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
