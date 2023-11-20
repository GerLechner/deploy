
from flask import Flask, render_template
from logging import FileHandler, WARNING
import sys
import os

app = Flask(__name__, template_folder = 'templates')
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/romper')
def romper():
    os._exit(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

