from fileinput import filename
from flask import Flask
from flask import render_template
from flask import url_for, redirect
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    print("Hello print")
    return "Hello return"
@app.route('/ola/<nome>')
def ola(nome):
    return f'Ola {nome}'

@app.route('/jp')
def jp():
    return 'Ola deu certo!'

produtos = {}

@app.route('/lista')
def listar():
    return produtos

@app.route('/adicionar/<item>/<valor>')
def adicionar(item,valor):
    produtos[item] = float(valor)
    return produtos

@app.route('/cadastro')
def cadastro():
    argunmentos = request.args.to_dict()
    print(argunmentos)

    return redirect(url_for('static', filename='formulario.html'))

    

if __name__ == "__main__":
    app.run()