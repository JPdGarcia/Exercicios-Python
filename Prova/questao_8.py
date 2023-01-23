# 8. Crie um programa que seja uma API de um contador de números. Esta API irá
# manter o número em sua memória, e esta irá iniciar com o valor 0 (zero).
# Para o programa teremos as seguinte chamadas:

from flask import Flask, request, jsonify

app = Flask(__name__)

contador = {"numero": 0}

@app.route('/contador', methods=['POST'])
def contador(contador):
    arg = request.get_json()
    numero = arg["numero"]
    contador = numero
    return jsonify(contador)

@app.route('/contador', methods=['GET'])
def mostra(contador):
    return jsonify(contador)

@app.route('/contador/incrementa', methods=['PUT'])
def incrementa(contador):
    arg = request.get_json()
    numero = arg["numero"]
    contador = contador + numero
    arg = request.get_json()
    return jsonify(contador)

@app.route('/contador', methods=['DELETE'])
def delete(contador):
    contador = 0
    return contador



if __name__ == "__main__":
    app.run(debug=True)