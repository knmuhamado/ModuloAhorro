from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/procesar_datos', methods=['POST'])
def procesar_datos():
    nombre = request.form['nombre']
    return jsonify({"mensaje Hola mundo"})

if __name__ == '__main__':
      app.run(debug=True)