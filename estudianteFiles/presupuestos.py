#Funciones para el manejo de presupuestos de los estudiantes

#Función para leer los presupuestos del txt
def leerPresupuestosE(nombre):
    #leer el archivo de presupuestos
    try:
        with open("estudianteFiles/archivosTxt/presupuestos.txt", "r") as archivo:
            presupuestos = eval(archivo.read())
            if nombre in presupuestos:
                return presupuestos[nombre]
            else:
                return {"alimentacion": 0, "transporte": 0, "Otros": 0, "Meta": 0}
    except Exception as e:
        print("Error al leer el archivo de presupuestos:", e)
        return {"alimentacion": 0, "transporte": 0, "Otros": 0, "Meta": 0}

"""Primero se abre el archivo de presupuestos.txt en modo lectura, se lee el contenido del mismo y con eval se evalua 
el archivo como un diccionario y se busca el nombre del estudiante. Si aparece se obtiene la información de presupuesto del mismo y si no 
se encuentra se devueleven el prespuestos con valores de cero"""

#Funcion para mostrar el presupuesto total
def mostrarTotalP(presupuesto):
    return sum(value for key, value in presupuesto.items() if key != 'Meta')

"""La función calcula y devuelve el presupuesto total de un estudiante, excluyendo la meta de ahorro. Esta 
itera sobre los items del presupuesto (presupuesto.items()), suma los valores de cada categoría, excepto la meta de ahorro 
(if key != 'Meta') y devuelve la suma total"""

#Función para editar el presupuesto por categorias
def editarPresupuestoE(name, categoria, nuevoPresupuesto):
    try:
        with open("estudianteFiles/archivosTxt/presupuestos.txt", "r") as archivo:
            presupuestos = eval(archivo.read())
        if name not in presupuestos:
            return False, "Usuario no encontrado"
        presupuestos[name][categoria] = int(nuevoPresupuesto)
        with open("estudianteFiles/archivosTxt/presupuestos.txt", "w") as archivo:
            archivo.write(str(presupuestos))
        return True, ""
    except Exception as e:
        return False, str(e)

"""En primer lugar la función abre el archivo presupuestos.txt en modo de lectura, lee el contenido del archivo y lo evalúa 
como un diccionario (eval(archivo.read())). Verifica si el nombre del estudiante existe en el diccionario, si no está, 
devuelve false y un mensaje de error. Esta actualiza el presupuesto de la categoría elegida con el nuevo valor
(presupuestos[name][categoria] = int(nuevoPresupuesto)) y actualiza el diccionario en el archivo presupuestos.txt 
en modo de escritur, devuelve true (verdadedoro) si la edición fue exitosa, o false y un mensaje de error si ocurrió un error"""
        
#Función para definir la meta de ahorro
def definirMeta(name, nuevaMeta):
    try:
        with open("estudianteFiles/archivosTxt/presupuestos.txt", "r") as archivo:
            presupuestos = eval(archivo.read())
        if name not in presupuestos:
            return False, "Usuario no encontrado"
        presupuestos[name]['Meta'] = int(nuevaMeta)
        with open("estudianteFiles/archivosTxt/presupuestos.txt", "w") as archivo:
            archivo.write(str(presupuestos))
        return True, ""
    except Exception as e:
        return False, str(e)

"""La función sigue los primeros pasos mencionados anteriormente: abrir, evaluar, buscar nombre, etc, y 
actualiza la meta de ahorro del estudiante con el nuevo valor (presupuestos[name]['Meta'] = int(nuevaMeta)). Escribe los cambios en el 
diccionario en el archivo presupuestos.txt en modo de escritura, devuelve true si la definición de la meta fue exitosa, 
o false y un mensaje de error si ocurrió un error"""
