from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap 

app = Flask(__name__)
#Se inicializa la extencion bootstrap para implementar una interfaz mas bonita
bootstrap = Bootstrap(app)

# se adiciona llave secreta para que tratar de manera encriptada la informacion del usuario
app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ['Cocinar', 'Barrer', 'Limpiar']


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    
    return response


@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos,
    }
    # al pasar el contexto es necesario utlizar ** para expandir el diccionario osea pasar cada una de las variables
    return render_template('hello.html', **context)