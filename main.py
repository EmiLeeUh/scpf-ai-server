import os
from flask import Flask, request, jsonify
import openai

# Create Flask app
app = Flask(__name__)

# Set OpenAI API key from Render environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/npc")
def npc():
    try:
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

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
