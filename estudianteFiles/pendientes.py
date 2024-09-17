#Función para ver los detalles de los pendientes
def obtener_pendientes(usuario):
    ruta_archivo = 'estudianteFiles/archivosTxt/pendientes.txt'
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            if contenido:
                pendientes = contenido.splitlines()
                # Filtrar pendientes por el nombre del usuario actual
                pendientes_usuario = [linea.split(',') for linea in pendientes if linea.split(',')[4] == usuario]
                return {'pendientes': pendientes_usuario}
            else:
                return {'pendientes': []}
    except FileNotFoundError:
        return {'pendientes': []}
    except Exception as e:
        return {"success": False, "message": str(e)}
        
"""Primero se lee el archivo pendientes.txt y se devuelve la lista de pendientes del usario especificado. Este archivo contiene lineas 
de texto con la estructura: fecha,id_pendiente,monto,nombre y usuario. La función filtra el contenido que corresponde al usuario 
específicado y devuelve una lista de listas, donde cada una contiene toda la información respecto a un pendiente"""

#Función para almacenar los pendientes en el archivo correspondiente
def guardar_pendientes(pendientes):
    ruta_archivo = 'estudianteFiles/archivosTxt/pendientes.txt'
    try:
        with open(ruta_archivo, 'w') as archivo:
            for pendiente in pendientes:
                pendiente_str = [str(elemento) for elemento in pendiente]
                archivo.write(','.join(pendiente_str) + '\n')
    except Exception as e:
        raise Exception(f"Error al guardar pendientes: {str(e)}")

"""Esta función toma un nuevo pendiente ingresado por el usario y lo almacena en el archivo de pendientes.txt, donde convierte la lista 
con detalles del pendiente en una cadena de texto y la escribe en el mencionado"""


#Función para agregar un nuevo pendiente
def añadir_pendiente(fecha, id_pendiente, monto, nombre, usuario):
    #se abre el archivo para añadir un nuevo pendiente
    ruta_archivo = 'estudianteFiles/archivosTxt/pendientes.txt'
    try:
        with open(ruta_archivo, 'a') as archivo:
            archivo.write(f"{fecha},{id_pendiente},{monto},{nombre},{usuario}\n")
    except Exception as e:
        raise Exception(f"Error al añadir pendiente: {str(e)}")
        
"""La función abre el archivo pendiente.txt en modo de escritura y escribe la nueva linea con los detalles del pendiente 
en el archivo"""


#Función para eliminar un pendiente
def eliminar_pendiente(id_pendiente, usuario):
    # se elimina un pendiente
    ruta_archivo = 'estudianteFiles/archivosTxt/pendientes.txt'
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            if contenido:
                pendientes = contenido.splitlines()
                pendientes = [linea for linea in pendientes if not (linea.split(',')[1] == id_pendiente and linea.split(',')[4] == usuario)]
                with open(ruta_archivo, 'w') as archivo:
                    for pendiente in pendientes:
                        archivo.write(pendiente + '\n')
    except Exception as e:
        raise Exception(f"Error al eliminar pendiente: {str(e)}")

"""Esta función lee el archivo de pendientes.txt y teniendo en cuenta el ID del pendiente y el usuario, filtra las lineas que no 
son del pendiente a eliminar y vuelve a escribir el archivo con las lineas restantes"""


"""Funciones y otras cosas utilizadas en el código: 
1. split(), función que permite dividir una cadena en una lista de subcadena separadas por un patrón especifico. 

Por ejemplo: está la cadena "hola,amigo,programador" y quieres dividirla en una lista de subcadenas separadas por comas, utilizas 
split de esta manera

cadena="hola,amigo,programador"
subcadenas = cadena.split(",")
print(subcadenas)  # Output: ["hola", "amigo", "programador"]

2. splitlines(), función que se utiliza para dividir el contenido del archivo en una lista de líneas. 

3. for variable in secuencia: 

Aquí la variable es aquella que se asignará a cada elemento de la secuencia en cada iteración, y secuencia es la lista 
o cadena que se va a iterar. La palabra in se utiliza para indicar que  la variable tomará el valor de cada elemento de 
la secuencia en cada iteración. 

4. try:
     código que puede generar una excepción
except TipoDeExcepcion: 
     código para manejar la excepción

except se utiliza para captura y manejar excepciones o errores que ocurran al ejecutar el código como el ingreso de una palabra incorrecta 
o así

5. raise, se usa para indicar que algo ha salido mal y que se debe terminar la ejecución. """

