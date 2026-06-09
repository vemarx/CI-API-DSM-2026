from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API CI/CD funcionando!"})

@app.route("/status")
def status():
    return jsonify({
        "status": "ok",
        "service": "CI API DSM"
    })

if __name__ == "__main__":
    app.run(debug=True)