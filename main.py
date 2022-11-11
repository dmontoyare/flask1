from flask import Flask, request

app = Flask(__name__)


@app.route('/hola')
def hello():
    user_ip = request.remote_addr
    return 'Hola, tu IP es {}'.format(user_ip)