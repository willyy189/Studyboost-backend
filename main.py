import openai
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# A chave da OpenAI vem da variável de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

@app.route('/processar', methods=['POST'])
def processar_texto():
    data = request.json
    texto = data.get('texto', '')

    if not texto:
        return jsonify({"erro": "Texto não fornecido"}), 400

    prompt = f"""
    Texto: {texto}

    Gera:
    1. Um resumo claro
    2. Flashcards (5 pares de pergunta e resposta)
    3. 5 perguntas de estudo para autoavaliação
    """

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        resultado = resposta.choices[0].message.content
        return jsonify({"resultado": resultado})
