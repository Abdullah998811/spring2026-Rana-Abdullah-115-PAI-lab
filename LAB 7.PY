from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Random Joke API is running"})

@app.route('/joke')
def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        joke = {
            "setup": data["setup"],
            "punchline": data["punchline"],
            "type": data["type"]
        }

        return jsonify(joke)
    else:
        return jsonify({"error": "Failed to fetch joke"}), 500


if __name__ == "__main__":
    app.run(debug=True)