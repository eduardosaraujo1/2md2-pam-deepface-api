from Analyze import analyze
from flask import Flask, request, jsonify
from flask_cors import CORS

# Criar aplicação FLASK
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hello, world!"

@app.route("/analyze", methods=["POST"])
def analyze_request():
    # Obter imagem do usuário
    data = request.get_json()

    # Validar se o campo correto existe
    if not "image" in data:
        return jsonify(message="Missing required parameter: 'image'"), 400

    # Efetuar análise através de analyze.py
    analysis = analyze(data['image'])

    return jsonify(analysis)


if (__name__ == '__main__'):
    # Prod: waitress-serve --host 127.0.0.1 main:app
    app.run(debug=True)