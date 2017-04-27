# -*- coding: utf-8 -*-

import sys, getopt
from Utilidades.Funciones import Funciones

def main(argv):
	try:
		if len(argv) > 0:
	  		opts, args = getopt.getopt(argv, "egat:r:s:i:", ["entrenar", "guardar", "ayuda", "test=", "rutaimg=", "sessionruta=", "intervalos="])

			funcion = Funciones()

			for opt, arg in opts:
				if opt in ("-a", "--ayuda"):
					print "Aqui debe ir las explciaciones de las variables"
				if opt in ("-g", "--guardar"):
					funcion.GuardarXML = True
				if opt in ("-e", "--entrenar"):
					funcion.Entrenar = True
				if opt in ("-i", "--intervalos"):
					funcion.Iteraciones = int(arg)
				if opt in ("-t", "--test"):
					funcion.RealizarTest = True
					funcion.RutaTest = arg
				if opt in ("-r", "--rutaimg"):
					funcion.RutaEntrenamiento = arg
				if opt in ("-s", "--sessionruta"):
					funcion.RutaSession = arg

			funcion.AjustarConfig()
			funcion.ValidarEntrenamiento()
			if funcion.RealizarTest == True:
				funcion.Prediccion()
		else:
			print "Debe ingresar al menos un parametro, consulte la guia de ayuada o digite -a para ver las opciones"	
	except getopt.GetoptError:          
		print "Opcion no valida"
		sys.exit(2)  

if __name__ == '__main__':
	main(sys.argv[1:])
