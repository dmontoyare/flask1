from flask import Flask

app = Flask(__name__)


@app.route('/hola')
def hello():
    return 'Hello World Flask'