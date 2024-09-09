from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/procesar_datos', methods=['GET'])
def procesar_datos():
    #Obtener datos del formulario

    return jsonify({"mensaje": "mensaje Hola mundo"})



if __name__ == '__main__':
      app.run(debug=True)