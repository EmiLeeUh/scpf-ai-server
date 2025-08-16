import os
from flask import Flask, request, jsonify
from openai import OpenAI

# Create Flask app
app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/npc")
def npc():
    try:
        data = request.json
        user_msg = data.get("message", "")
        player = data.get("player", "")
        personality = data.get("personality", "Calm, observant, slightly cryptic")
        recent_context = data.get("recentContext", "")

        # Build prompt for Mira
        prompt = f"You are Mira, {personality}.\nRecent conversation: {recent_context}\nPlayer {player} says: {user_msg}\nReply:"

        # Use new OpenAI chat API
        response = client.chat.completions.create(
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
