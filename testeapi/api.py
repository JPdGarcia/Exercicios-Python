from flask import Flask, send_from_directory
import os
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return '<a href = "/Estatistica_gama.csv"> Download arquivo</a>'

@app.route('/<path:arquivo>')
def download(arquivo):
    diretorio = '/home/jop_garcia/Documentos/Gama_Magalu_exercicios/testeapi/'
    return send_from_directory(diretorio, arquivo, as_attachment=True)
    

if __name__ == '__main__':
    app.run(debug = True)

    '''for file_name in os.listdir(directory):
            id_arquivo = os.path.join(directory, file_name)
            if(os.path.isfile(id_arquivo)):
                file.append(file_name)
'''