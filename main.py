from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def handle_message(data):
    user_message = data["message"]
    bot_response = f"Echo: {user_message}"  # Replace this with an API call to a cloud-based AI
    emit("response", {"message": bot_response})

@app.route("/")
def home():
    return "AI Messenger Running Online!"

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
