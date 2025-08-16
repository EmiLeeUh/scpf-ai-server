import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure your key is set in secrets

@app.post("/npc")
def npc():
    user_msg = request.json.get("message", "")
    player = request.json.get("player", "")
    personality = request.json.get("personality", "Calm, observant, slightly cryptic")
    recent_context = request.json.get("recentContext", "")

    prompt = f"You are Mira, {personality}.\nRecent conversation: {recent_context}\nPlayer {player} says: {user_msg}\nReply:"

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )

    reply = response.choices[0].message.content.strip()
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
