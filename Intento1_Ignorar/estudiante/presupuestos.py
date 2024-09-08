from django.core.serializers import json


# Funciones para el manejo de presupuestos
def leerPresupuestos():
    try:
        with open("presupuestos.txt", "r") as archivo:
            lines = archivo.readlines()
            return {
                "alimentacion": int(lines[0].strip()),
                "transporte": int(lines[1].strip()),
                "vivienda": int(lines[2].strip()),
                "implementos": int(lines[3].strip())
            }
    except FileNotFoundError:
        return {"alimentacion": 0, "transporte": 0, "vivienda": 0, "implementos": 0}

def guardarPresupuestos(presupuestos):
    with open("presupuestos.txt", "w") as archivo:
        archivo.write(f"{presupuestos['alimentacion']}\n")
        archivo.write(f"{presupuestos['transporte']}\n")
        archivo.write(f"{presupuestos['vivienda']}\n")
        archivo.write(f"{presupuestos['implementos']}\n")


#funcion para añadir o actualizar el presupuesto de alimentacion en el txt
def pAlimentacion(int):
    with open("presupuestos.txt", "w") as archivo:
        archivo.write(str(int))
        print(f"El presupuesto de alimentacion es: {int}")
        return int

#funcion para añadir o actualizar el presupuesto de transporte en el txt
def pTransporte(int):
    with open("presupuestos.txt", "w") as archivo:
        archivo.write(str(int))
        print(f"El presupuesto de transporte es: {int}")
        return int

#funcion para añadir o actualizar el presupuesto de vivienda en el txt
def pVivienda(int):
    with open("presupuestos.txt", "w") as archivo:
        archivo.write(str(int))
        print(f"El presupuesto de vivienda es: {int}")
        return int

#funcion para añadir o actualizar el presupuesto de implementos en el txt
def pImplementos(int):
    with open("presupuestos.txt", "w") as archivo:
        archivo.write(str(int))
        print(f"El presupuesto de implementos es: {int}")
        return int

#funcion para guardar la meta de ahorro
def metaAhorro(int):
    with open("presupuestos.txt", "w") as archivo:
        archivo.write(str(int))
        print(f"La meta de ahorro es: {int}")
        return int

#funcion para mostrar el presupuesto total
def mostrarTotal():
    presupuestos = leerPresupuestos()
    total = sum(presupuestos.values())
    return total

