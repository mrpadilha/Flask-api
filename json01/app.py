from flask import Flask, jsonify, request


app = Flask(__name__)

devs = [
    {
        'id': 1,
        'nome': 'Rafael Marques',
        'linguagem': 'PHP'
    },

    {
        'id': 2,
        'nome:': 'Gilberto',
        'linguagem': 'Python'
    }



]

@app.route('/devs', methods =['GET'])
def home():
    return jsonify(devs), 200

@app.route('/devs/<string:linguagem>', methods =['GET'])
def devs_per_linguagem(linguagem):
    devs_per_linguagem = [dev for dev in devs if dev['linguagem'] == linguagem]
    return jsonify(devs_per_linguagem), 200

@app.route('/devs/<int:id>', methods = ['GET'])
def devs_per_id(id):
    for dev in devs:
        if dev ['id'] == id:
            return jsonify (dev), 200
    return jsonify ({'Erro': 'Nao encontrado'}), 404

@app.route('/devs', methods = ['POST'])
def save_dev():
    data = request.get_json()

    devs.append(data)
    return jsonify(data), 201



if __name__ == '__main__':
    app.run(debug=True)