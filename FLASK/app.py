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

produtos = {}
serie = pd.DataFrame()

@app.route('/lista')
def listar():
    return serie

@app.route('/cadastro')
def cadastro():
    argumentos = request.args.to_dict()
    print(argumentos)
    #produto = argumentos['produto']
    #preço = argumentos['preço']
    #serie[produto] = preço
    
    serie.to_csv('produtos.csv', header=False)
    return redirect(url_for('static', filename='formulario.html'))

    
if __name__ == "__main__":
    app.run()