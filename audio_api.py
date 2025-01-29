from flask import Flask, request, Response
from flask_cors import CORS
from gtts import gTTS
import io

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

@app.route('/',methods=['GET'])
def welcome():
    return "<h1>Welcome to Telugu Bible audio<h1>"

@app.route("/text-to-speech/", methods=["POST"])
def text_to_speech():
    text = request.form.get("text")
    if not text:
        return {"error": "Text is required"}, 400

    audio_io = io.BytesIO()
    tts = gTTS(text=text, lang="te")
    tts.write_to_fp(audio_io)
    audio_io.seek(0)  # Move pointer to the start

    return Response(audio_io, mimetype="audio/mpeg", headers={"Content-Disposition": "inline; filename=output.mp3"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
