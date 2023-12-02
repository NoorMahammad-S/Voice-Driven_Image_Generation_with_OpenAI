from flask import Flask, render_template, request
from flask_socketio import SocketIO
import openai
import speech_recognition as sr
import threading
import time
import os

app = Flask(__name__)
socketio = SocketIO(app)

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Use environment variable for API key


def capture_voice():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None


def gpt3_text_understanding(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=100
    )
    return response.choices[0].text.strip()


def dalle_image_generation(prompt):
    response = openai.Image.create(
        model="image-alpha-001",
        prompt=prompt,
        n=1
    )
    image_url = response['data'][0]['url']
    return image_url


def simulate_real_time_interaction(image_url):
    for i in range(1, 6):
        time.sleep(2)  # Simulate processing time
        socketio.emit('update', f"Update {i}: Processing...")

    socketio.emit('update', f"Image generated: {image_url}")


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('voice_input')
def handle_voice_input():
    voice_input = capture_voice()

    if voice_input:
        gpt3_output = gpt3_text_understanding(voice_input)
        dalle_output = dalle_image_generation(gpt3_output)

        threading.Thread(target=simulate_real_time_interaction, args=(dalle_output,)).start()


if __name__ == '__main__':
    socketio.run(app, debug=True)
