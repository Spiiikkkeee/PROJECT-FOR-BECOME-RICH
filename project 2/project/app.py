from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Flask app and SocketIO intialization

app = Flask(__name__)

socketio = SocketIO(app)

@app.route("/")

def index():
    return render_template("index.html")

def index():
    return render_template("style.css")


@socketio.on("play")

def play_event(data):
    emit("pause", broadcast=True)

@socketio.on("sync")
def sync_event(data):
    emit("sync", data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)