from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "Bienvenido a Pacific DevOps Music Fest API"
    })

@app.route("/api")
def concierto():
    return jsonify({
        "festival": "Pacific DevOps Music Fest",
        "fecha": "15 Agosto 2026",
        "artistas": [
            "Imagine Dragons",
            "Coldplay",
            "Linkin Park"
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)