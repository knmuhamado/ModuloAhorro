#Funciones para el manejo de presupuestos de los estudiantes

#funcion para leer los presupuestos del txt
def leerPresupuestosE(nombre):
    try:
        with open("estudianteFiles/presupuestos.txt", "r") as archivo:
            presupuestos = eval(archivo.read())
            if nombre in presupuestos:
                return presupuestos[nombre]
            else:
                return {"alimentacion": 0, "transporte": 0, "Entretenimiento": 0, "Meta": 0}
    except Exception as e:
        print("Error al leer el archivo de presupuestos:", e)
        return {"alimentacion": 0, "transporte": 0, "Entretenimiento": 0, "Meta": 0}


#funcion para mostrar el presupuesto total
def mostrarTotalP(presupuesto):
    return sum(value for key, value in presupuesto.items() if key != 'Meta')

#funcion para editar el presupuesto por categorias
def editarPresupuestoE(name, categoria, nuevoPresupuesto):
    try:
        with open("estudianteFiles/presupuestos.txt", "r") as archivo:
            presupuestos = eval(archivo.read())
        if name not in presupuestos:
            return False, "Usuario no encontrado"
        presupuestos[name][categoria] = int(nuevoPresupuesto)
        with open("estudianteFiles/presupuestos.txt", "w") as archivo:
            archivo.write(str(presupuestos))
        return True, ""
    except Exception as e:
        return False, str(e)






