from flask import Flask, request, jsonify

# Memory now tracks each player individually
memory = {}

def ai_response(player, message):
    # Initialize memory for the player if not exists
    if player not in memory:
        memory[player] = []

    # Save message to this player's memory
    memory[player].append(message)

    # Simple logic
    if "hello" in message.lower():
        return f"Hello, {player}. How can I assist you today?"
    elif "status" in message.lower():
        return "All systems are running normally."
    elif "memory" in message.lower():
        return f"I remember your messages: {memory[player]}"
    else:
        return f"(AI) You said: {message}"

app = Flask(__name__)

@app.get("/ping")
def ping():
    return "pong"

@app.post("/npc")
def npc():
    # Expecting JSON: { "player": "<name>", "message": "<text>" }
    data = request.json
    player = data.get("player", "Unknown")
    user_msg = data.get("message", "")
    reply = ai_response(player, user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
