#Funciones para el manejo de presupuestos de los estudiantes


#funcion para leer los presupuestos del txt
def leerPresupuestosH(nombre):
    #leer el archivo de presupuestos
    try:
        with open("hogarFiles/archivosTxt/presupuestos.txt", "r") as archivo:
            presupuestos = eval(archivo.read())
            if nombre in presupuestos:
                return presupuestos[nombre]
            else:
                return {"alimentacion": 0, "vivienda": 0,"servicios":0, "Otros": 0, "Meta": 0}
    except Exception as e:
        print("Error al leer el archivo de presupuestos:", e)
        return {"alimentacion": 0, "vivienda": 0,"servicios":0, "Otros": 0, "Meta": 0}


#funcion para mostrar el presupuesto total
def mostrarTotalP(presupuesto):
    return sum(value for key, value in presupuesto.items() if key != 'Meta')


#funcion para editar el presupuesto por categorias
def editarPresupuestoH(name, categoria, nuevoPresupuesto):
    try:
        with open("hogarFiles/archivosTxt/presupuestos.txt", "r") as archivo:
            presupuestos = eval(archivo.read())
        if name not in presupuestos:
            return False, "Usuario no encontrado"
        presupuestos[name][categoria] = int(nuevoPresupuesto)
        with open("hogarFiles/archivosTxt/presupuestos.txt", "w") as archivo:
            archivo.write(str(presupuestos))
        return True, ""
    except Exception as e:
        return False, str(e)


#funcion para definir la meta de ahorro
def definirMeta(name, nuevaMeta):
    try:
        with open("hogarFiles/archivosTxt/presupuestos.txt", "r") as archivo:
            presupuestos = eval(archivo.read())
        if name not in presupuestos:
            return False, "Usuario no encontrado"
        presupuestos[name]['Meta'] = int(nuevaMeta)
        with open("hogarFiles/archivosTxt/presupuestos.txt", "w") as archivo:
            archivo.write(str(presupuestos))
        return True, ""
    except Exception as e:
        return False, str(e)

