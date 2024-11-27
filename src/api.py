from flask import Flask, request, jsonify
from flask_cors import CORS
from src.analyze import analyze

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
        return jsonify(error="Missing required parameter: 'image'"), 400

    # Efetuar análise através de analyze.py
    analysis = analyze(data['image'])

    # Se analize for invalida, retornar erro
    if not analysis:
        return jsonify(error="Internal analysis error")

    return jsonify(analysis)

