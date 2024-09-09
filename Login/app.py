from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/procesar_datos', methods=['POST'])
def procesar_datos():
    # Obtener datos del formulario
    data = request.get_json()
    nombre = data.get('nombre')

    return jsonify({"mensaje": nombre})


if __name__ == '__main__':
      app.run(debug=True)