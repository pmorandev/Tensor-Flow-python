from Utilidades.Generales.Archivos import *

def CantidadArgumentos(argv):
	respuesta = True
	mensaje = ""
	if len(argv) == 0:
        	mensaje = "La cantidad de argumentos ingresada no es correcta" 
		respuesta = False
	return respuesta, mensaje

def ExisteCarpeta(imagenes):
	return ExisteArchivo(imagenes)
