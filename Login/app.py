from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def verificarUsuario(nombre, contrasena):
     # Diccionario con usuarios

    usuarios = {
        "usuario1": {
            "nombre": "Juan",
            "contrasena":"1234",
            "perfil": "Estudiante",
        },
        "usuario2": {
            "nombre": "Ana",
            "contrasena":"1432",
            "perfil": "Estudiante"
        },
        "usuario3": {
            "nombre": "Maria",
            "contrasena":"2431",
            "perfil": "Hogar",
        }, 
        "usuario4": {
            "nombre": "Laura",
            "contrasena":"2431",
            "perfil": "Hogar",
        },
    }

    for usuario in usuarios.values():
        if  usuario["nombre"] and usuario["contrasena"] == contrasena:
            if usuario["perfil"] == "Estudiante":
                return "../Intento1_ignorar/estudiante.html"
            else:
                return "hogar"
    return False
    
@app.route('/procesar_datos', methods=['POST'])
def procesar_datos():
    # Obtener datos del formulario
    data = request.get_json()
    nombre = data.get('nombre')
    contrasena = data.get('contrasena')
    resultado=verificarUsuario(nombre,contrasena)

    if resultado != False:
        return jsonify({"mensaje": "Acceso permitido", "perfil": resultado})
    else:
        return jsonify({"mensaje": "Acceso denegado"})

   


if __name__ == '__main__':
      app.run(debug=True)