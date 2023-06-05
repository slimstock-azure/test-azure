import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
def run_server():
    app = Flask(__name__)

    @app.route('/')
    def index():
        print('Request for index page received')
        return render_template('index.html')

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

    if __name__ == '__main__':
        app.run()