from flask import render_template, redirect, url_for, request
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


if __name__ == '__main__':
    app.run()
