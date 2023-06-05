import os
import logging
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

def define_server():
    app = Flask(__name__)


    @app.route('/')
    def index():
       logging.info("Requested index.html")
       logging.info("Environment variables: " + '\n'.join([f'{k}: {v}' for k, v in sorted(os.environ.items())]))
       print('test')
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