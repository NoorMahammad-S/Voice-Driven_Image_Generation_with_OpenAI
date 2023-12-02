# Voice-Driven Image Generation with OpenAI

This Flask application captures voice input, processes it using OpenAI's GPT-3 and DALL-E models, and generates an image based on the processed text. Real-time updates are sent to the UI using Flask-SocketIO.

## Setup

1. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set up your OpenAI API key:

   - Obtain an API key from [OpenAI](https://beta.openai.com/signup/).
   - Set the API key as an environment variable named `OPENAI_API_KEY`.

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Access the application in your web browser at [http://localhost:5000/](http://localhost:5000/).

3. Click the "Start Recording" button to initiate voice input. Real-time updates will be displayed on the UI.

## Customization

- **OpenAI Models**: You can customize the OpenAI models used in the `gpt3_text_understanding` and `dalle_image_generation` functions according to your preferences.

- **Environment Variables**: Ensure that you set any necessary environment variables, especially `OPENAI_API_KEY`.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests.

