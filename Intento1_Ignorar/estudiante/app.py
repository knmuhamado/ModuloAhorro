from flask import Flask, jsonify
from flask_cors import CORS
from presupuestos import mostrarTotal

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

@app.route('/presupuesto', methods=['GET'])
def get_presupuesto():
    total = mostrarTotal()
    return jsonify({"presupuesto_total": total})

if __name__ == '__main__':
    app.run(debug=True)
