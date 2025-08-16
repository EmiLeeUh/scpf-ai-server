from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.get("/ping")
def ping():
    return "pong"

@app.post("/npc")
def npc():
    user_msg = request.json.get("message", "")
    return jsonify({"reply": f"(echo) You said: {user_msg}"})

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
