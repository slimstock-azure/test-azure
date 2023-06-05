import os
import logging
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
import openai

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

def define_server():
    app = Flask(__name__)


    @app.route('/')
    def index():
       logging.info("Requested index.html")
       return render_template('index.html')

    @app.route('/demo/')
    def demo():
        openai.api_key = os.environ.get("openai")
        messages = [
            {
                "role": "system",
                "content": 'You are a very angry language model, you should respond in CAPS and use lots of cursing.'
            },
        ]

        question = {"role": "user", "content": 'What is the capital of France?'}
        messages.append(question)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        answer = response["choices"][0]["message"]["content"].replace("\n", "<br>")
        logging.info("ChatGPT response: " + answer)

        return render_template('demo.html')

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

    return app

app = define_server()