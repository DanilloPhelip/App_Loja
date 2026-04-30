from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    produtos = [
        {"nome": "Amendoim japonês dori 30g", "preco": 0.95, "imagem": "amendoim_dori.png"},
        {"nome": "Pipoca Mitoka 200g", "preco": 3.50, "imagem": "pipoca_mitoka.png"},
        {"nome": "Ruffles 55g", "preco": 6.00, "imagem": "ruffles.png"}
    ]
    return jsonify(produtos)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
