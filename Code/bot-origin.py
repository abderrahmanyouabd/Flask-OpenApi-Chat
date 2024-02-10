from flask import Flask, render_template, request
from BotDefinition import OpenAIBot

# Creating the Flask App
app = Flask(__name__)

chatbot = OpenAIBot("gpt-3.5-turbo")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():

    prompt = request.form['prompt']

    if prompt.upper() == 'END CHAT':
        return 'END CHAT'

    response = chatbot.generate_response(prompt)
    return response


if __name__ == '__main__':
    app.run(debug=True)
