from flask import Flask

app = Flask(__name__)

@app.route('/')
def api():
    return {"mensagem": "ola"}

if __name__ =="__main__":
    app.run(debug=True)
