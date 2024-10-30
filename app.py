from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/matricula", methods=['POST'])
def envio():
    data = request.get_json()
    nome = data.get('nome')
    ra = data.get('ra')
    idade = data.get('idade')

    return jsonify({'message:' f'Recebido: {nome}, RA: {ra} e Idade: {idade}'}), 200


if __name__ == "__main__":
    app.run(debug=True)