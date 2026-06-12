from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api")
def concierto():
    return jsonify({
        "festival":"Pacific DevOps Music Fest",
        "fecha":"15 Agosto 2026",
        "artistas":[
            "Imagine Dragons",
            "Coldplay",
            "Linkin Park"
        ]
    })

app.run(host="0.0.0.0", port=5000)