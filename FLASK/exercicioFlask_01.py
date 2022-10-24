from fileinput import filename
from multiprocessing.sharedctypes import Value
from optparse import Values
from flask import Flask
from flask import render_template
from flask import url_for, redirect
from flask import request
import pandas as pd

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
serie = pd.DataFrame()



@app.route('/adicionar/<item>/<valor>')
def adicionar(item,valor):
    produtos[item] = float(valor)
    return produtos

@app.route('/cadastro')
def cadastro():
    argumentos = request.args.to_dict()
    print(argumentos)
    #produto = argumentos['produto']
    #preco = argumentos['preco']
    #serie[produto] = preco
    #serie.to_csv('produtos.csv', header=False)
    
    #return redirect(url_for('static', filename='formulario.html'))
    return argumentos

    

if __name__ == "__main__":
    app.run()