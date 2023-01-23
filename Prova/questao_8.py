# 8. Crie um programa que seja uma API de um contador de números. Esta API irá
# manter o número em sua memória, e esta irá iniciar com o valor 0 (zero).
# Para o programa teremos as seguinte chamadas:

from flask import Flask, request, jsonify
import json

app = Flask(__name__)


with open("contador.json", "r") as json_file:
    contador = json.load(json_file)


@app.route('/contador', methods=['POST'])
def contador():
    global contador
    arg = request.get_json()
    numero = arg["numero"]
    contador = numero
    return jsonify(contador), 201

@app.route('/contador', methods=['GET'])
def mostra():
    global contador
    return jsonify(contador), 200

@app.route('/contador/incrementa', methods=['PUT'])
def incrementa():
    global contador
    arg = request.get_json()
    numero = arg["numero"]
    contador = contador + numero
    arg = request.get_json()
    return jsonify(contador), 202

@app.route('/contador', methods=['DELETE'])
def delete():
    global contador
    contador = 0
    return contador



if __name__ == "__main__":
    app.run(debug=True), 202