# Funciones para manejar los gastos de los estudiantes

#Funciones para manejar los gastos de los estudiantes
def leerGastosE(nombre):
    try:
        with open("estudianteFiles/archivosTxt/gastos.txt", "r") as archivo:
            gastos = eval(archivo.read()) 
            if nombre in gastos:
                return gastos[nombre]
            else:
                return {"alimentacion": [0], "transporte": [0], "Otros": [0], "Ahorro": 0}
    except Exception as e:
        print("Error al leer el archivo de gastos:", e)
        return {"alimentacion": [0], "transporte": [0], "Otros": [0], "Ahorro": 0}

"""Primero se lee el archivo de gastos.txt, que contiene la información de los gastos de los estudiantes. Este archivo contiene un 
diccionario donde se almacenan los nombres de los estudiantes y sus gastos, este se puede evaluar con la función eval(), la cual busca 
el nombre en el archivo y devuelve los gastos de la persona, así pues si el nombre no es encontrado se devuelven los valores de gasto con
el valor predeterminado de 0"""

#funcion para mostrar el total de lo gastado
def mostrarTotalGastos(gastos):
    #se suman los valores de cada lista en cada categoria excepto la de ahorro
    gastosTotales = sum(sum(value) for key, value in gastos.items() if key != 'Ahorro')
    return gastosTotales

#funcion para añadir gastos por categorias
def añadirGastoE(usuario, categoria, nuevoGasto):
    try:
        with open("estudianteFiles/archivosTxt/gastos.txt", "r") as archivo:
            gastos = eval(archivo.read())
        if usuario not in gastos:
            return False, "Usuario no encontrado"
        if len(gastos[usuario][categoria]) >= 1:
            gastos[usuario][categoria].append(int(nuevoGasto))
        else:
            gastos[usuario][categoria] = [int(nuevoGasto)]
        with open("estudianteFiles/archivosTxt/gastos.txt", "w") as archivo:
            archivo.write(str(gastos))
        return True, ""
    except Exception as e:
        return False, str(e)

"""Primero se lee el archivo, se evalua y se busca el usario, en caso de no encontrarlo retorna falso y el mensaje de que el usario 
no me fue encontrado, y la categoría correspondiente. Si en la categoría ya existía al menos un elemento se agrega el nuevo gasto, de lo
contrario se crea una nueva lista con el nuevo gasto. Para finalizar se actualiza el diccionario en el archivo txt"""

#funcion para sumar ahorro

def sumarAhorro(usuario, ahorro):
    try:
        with open("estudianteFiles/archivosTxt/gastos.txt", "r") as archivo:
            gastos = eval(archivo.read())
        if usuario not in gastos:
            return False, "Usuario no encontrado"
        gastos[usuario]['Ahorro'] += int(ahorro)
        with open("estudianteFiles/archivosTxt/gastos.txt", "w") as archivo:
            archivo.write(str(gastos))
        return True, ""
    except Exception as e:
        return False, str(e)

"""Primero se lee el archivo, se evalua y se busca al usario, en caso de no encontrarse se retorna falso y el mensanje de usuario no 
encontrado. Posterior a eso se suma el monto especificado de gastos a la categoría de ahorro y se actualiza el archivo gasto.txt"""


#funcion para restar ahorro
def restarAhorro(usuario, ahorro):
    try:
        with open("estudianteFiles/archivosTxt/gastos.txt", "r") as archivo:
            gastos = eval(archivo.read())
        if usuario not in gastos:
            return False, "Usuario no encontrado"
        gastos[usuario]['Ahorro'] -= int(ahorro)
        with open("estudianteFiles/archivosTxt/gastos.txt", "w") as archivo:
            archivo.write(str(gastos))
        return True, ""
    except Exception as e:
        return False, str(e)

"""Se hace el mismo proceso que en la función sumarAhorro, pero esta vez se resta el monto especificado"""

#funcion para editar ahorro
def editar_Ahorro(usuario, opcion, ahorro):
    try:
        if opcion == "retirar":
            return restarAhorro(usuario, ahorro)
        elif opcion == "Añadir":
            return sumarAhorro(usuario, ahorro)
    except Exception as e:
        return False, str(e)

"""Es una función que sirve para que al elegir la opción de retirar se llame la función restarAhorro o si se elige añadir se llame a 
la función sumarAhorro, si no se elige alguna de las dos mencionadas se retorna falso y se maneja la exepción"""

#Funcion para sumar gastos por categorias
def sumarGastos(usuario):
    try:
        with open("estudianteFiles/archivosTxt/gastos.txt", "r") as archivo:
            gastos = eval(archivo.read())
        if usuario not in gastos:
            return False, "Usuario no encontrado"
        gastosS= { "Alimentacion": sum(gastos[usuario]["Alimentacion"]), "Transporte": sum(gastos[usuario]["Transporte"]), "Otros": sum(gastos[usuario]["Otros"]), "Ahorro": gastos[usuario]["Ahorro"]}
        return gastosS
    except Exception as e:
        return False, str(e)

"""Para efectuar la suma de los gastos de las categorías esta función lee el archivo gastos.text, busca al usuario suma los valores de
cada lista en cada categoría. Por último devuelve el diccionario con los resultados de esta suma"""
