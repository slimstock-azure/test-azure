import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

def define_server():
    app = Flask(__name__)


    @app.route('/')
    def index():
       print('Request for index page received')
       return render_template('index.html')

    @app.route('/demo/')
    def demo():
        return render_template('demo.html')

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

    return app

app = define_server()