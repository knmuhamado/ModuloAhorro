from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from estudianteFiles.presupuestos import mostrarTotalP, leerPresupuestosE, editarPresupuestoE
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
        return jsonify({"presupuesto_total": totalP, "gastado": gastado, "presupuestos": leerPresupuestosE(name), "gastos": leerGastosE(name)})

@app.route('/editar_presupuesto', methods=['POST'])
def editar_presupuesto():
    data = request.get_json()
    usuario = name
    categoria = data.get('categoria')
    nuevo_presupuesto = data.get('nuevoPresupuesto')

    if not categoria or not nuevo_presupuesto:
        return jsonify({"success": False, "message": "Datos incompletos"}), 400

    try:
        exito, mensaje = editarPresupuestoE(usuario, categoria, nuevo_presupuesto)
        if exito:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": mensaje}), 500
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500



@app.route('/editar_gasto', methods=['POST'])
def editar_gasto():
    data = request.get_json()
    usuario = name
    categoria = data.get('categoria')
    nuevo_gasto = data.get('nuevoGasto')

    if not categoria or not nuevo_gasto:
        return jsonify({"success": False, "message": "Datos incompletos"}), 400

    try:
        # Leer el archivo de gastos
        with open("estudianteFiles/gastos.txt", "r") as archivo:
            gastos = json.load(archivo)

        # Verificar si el usuario existe en el archivo
        if usuario not in gastos:
            return jsonify({"success": False, "message": "Usuario no encontrado"}), 404

        # Verificar si la categoría existe para ese usuario
        if categoria not in gastos[usuario]:
            return jsonify({"success": False, "message": "Categoría no encontrada"}), 404

        if not isinstance(gastos[usuario][categoria], list):
            return jsonify({"success": False, "message": "El formato de la categoría no es una lista"}), 400


        # Actualizar el gasto de la categoría seleccionada para ese usuario
        gastos[usuario][categoria].append(int(nuevo_gasto))

        # Guardar los cambios en el archivo
        with open("estudianteFiles/gastos.txt", "w") as archivo:
            json.dump(gastos, archivo)

        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
