from flask import Flask, request, jsonify

# Simple memory for the AI (in-memory for now)
memory = []

def ai_response(message):
    # Save the message to memory
    memory.append(message)

    # Simple logic based on keywords
    if "hello" in message.lower():
        return "Hello, agent. How can I assist you today?"
    elif "status" in message.lower():
        return "All systems are running normally."
    elif "memory" in message.lower():
        return f"I remember these messages: {memory}"
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
