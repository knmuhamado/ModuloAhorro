from flask import Flask, jsonify, request
from flask_cors import CORS
from estudianteFiles.presupuestos import mostrarTotalP, leerPresupuestosE
from estudianteFiles.gastos import leerGastosE, mostrarTotalGastos


app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

name = None
def verificarUsuario(nombre, contrasena):
    # Diccionario con usuarios
    usuarios = {
        "usuario1": {
            "nombre": "Juan",
            "contrasena": "1234",
            "perfil": "Estudiante",
        },
        "usuario2": {
            "nombre": "Ana",
            "contrasena": "1432",
            "perfil": "Estudiante"
        },
        "usuario3": {
            "nombre": "Maria",
            "contrasena": "2431",
            "perfil": "Hogar",
        },
        "usuario4": {
            "nombre": "Laura",
            "contrasena": "2431",
            "perfil": "Hogar",
        },
    }

    for usuario in usuarios.values():
        if usuario["nombre"] == nombre and usuario["contrasena"] == contrasena:
            return usuario["perfil"]
    return False


@app.route('/procesar_datos', methods=['POST'])
def procesar_datos():
    # Obtener datos del formulario
    data = request.get_json()
    nombre = data.get('nombre')
    contrasena = data.get('contrasena')
    resultado = verificarUsuario(nombre, contrasena)

    if resultado:
        global name
        name = nombre
        if resultado == "Estudiante":
            presupuesto = leerPresupuestosE(nombre)
            gastos = leerGastosE(nombre)
        else:
            presupuesto = None
            gastos = None
        if presupuesto:
            return jsonify({
                "mensaje": "Acceso permitido",
                "perfil": resultado,
                "presupuesto": presupuesto,
                "gastos": gastos
            })
        else:
            return jsonify({"mensaje": "Acceso permitido, pero no se encontró presupuesto"})
    else:
        return jsonify({"mensaje": "Acceso denegado"})


@app.route('/datos', methods=['GET'])
def get_presupuesto():
    if name is None:
        return jsonify({"mensaje": "No se ha iniciado sesión"})
    else:
        gastado = mostrarTotalGastos(leerGastosE(name))
        totalP = mostrarTotalP(leerPresupuestosE(name))
        return jsonify({"presupuesto_total": totalP, "gastado": gastado})


if __name__ == '__main__':
    app.run(debug=True)
