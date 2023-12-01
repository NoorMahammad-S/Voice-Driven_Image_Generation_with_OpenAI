from flask import Flask, render_template
import openai
import speech_recognition as sr
import time

app = Flask(__name__)

# Set up your OpenAI API keys
openai.api_key = "YOUR_OPENAI_API_KEY"

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
    updates = []

    for i in range(1, 6):
        updates.append(f"Update {i}: Processing...")
        time.sleep(2)  # Simulate processing time

    updates.append(f"Image generated: {image_url}")
    return updates

@app.route('/')
def index():
    voice_input = capture_voice()

    if voice_input:
        gpt3_output = gpt3_text_understanding(voice_input)
        dalle_output = dalle_image_generation(gpt3_output)
        updates = simulate_real_time_interaction(dalle_output)

        return render_template('index.html', updates=updates, image_url=dalle_output)

if __name__ == '__main__':
    app.run(debug=True)
