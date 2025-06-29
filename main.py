from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Believe in yourself.",
    "You got this!",
    "Every expert was once a beginner.",
    "Keep coding, it gets better.",
    "Trust the process."
]

@app.route("/quote")
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
