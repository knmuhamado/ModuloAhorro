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


def guardar_pendientes(pendientes):
    ruta_archivo = 'estudianteFiles/archivosTxt/pendientes.txt'
    try:
        with open(ruta_archivo, 'w') as archivo:
            for pendiente in pendientes:
                pendiente_str = [str(elemento) for elemento in pendiente]
                archivo.write(','.join(pendiente_str) + '\n')
    except Exception as e:
        raise Exception(f"Error al guardar pendientes: {str(e)}")

def añadir_pendiente(fecha, id_pendiente, monto, nombre, usuario):
    #se abre el archivo para añadir un nuevo pendiente
    ruta_archivo = 'estudianteFiles/archivosTxt/pendientes.txt'
    try:
        with open(ruta_archivo, 'a') as archivo:
            archivo.write(f"{fecha},{id_pendiente},{monto},{nombre},{usuario}\n")
    except Exception as e:
        raise Exception(f"Error al añadir pendiente: {str(e)}")


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
