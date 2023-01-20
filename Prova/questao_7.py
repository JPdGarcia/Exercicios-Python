# 7. Crie uma API Rest em Python, que responda à seguinte chamada:
# curl -X POST 'http://localhost:5000/soma' -H 'Content-type:
# application/json' -d '{"x": 1, "y"; 2}'

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/soma', methods=['POST'])
def soma():
    arg = request.get_json()
    x = arg['x']
    y = arg['y']
    result = x + y
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)