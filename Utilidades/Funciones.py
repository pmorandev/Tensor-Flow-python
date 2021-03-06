from Generales.Archivos import *
from DataSet.Datos import DataSet
from Configuracion.Config import Config
from Tensor.Modelo.Modelo import Modelo
from Tensor.Prediccion.Prediccion import Prediccion
from Tensor.Utilidades.Imagenes import *

class Funciones:
	def __init__(self):
		self.RealizarTest = False
		self.RutaTest = ""
		self.Entrenar = False
		self.RutaEntrenamiento = ""
		self.RutaSession = ""
		self.GuardarXML = False
		self.Iteraciones = 0
		self.Config = Config()

	def EntrenarModelo(self):
		self.Datos = DataSet(self.Config)
		self.Datos.LeerArchivos()
		self.Datos.Cargar_Imagenes()
		self.Datos.Cargar_Etiquetas()
		self.Datos.Config.ETI_CONTEO = len(self.Datos.DT_Predicciones)
		self.Modelo = Modelo(self.Datos)
	
	def ValidarEntrenamiento(self):
		if self.Entrenar == False:
			if ExistePrediccionCSV(self.Config.RT_ENTRENAMIENTO) == True:
				if ExisteSession(self.Config.RT_ESTADOSESSION) == True:
					self.Datos = DataSet(self.Config)
					self.Datos.Cargar_Predicciones()
					if int(self.Config.ETI_CONTEO) != len(self.Datos.DT_Predicciones):
						self.EntrenarModelo()
				else:
					self.EntrenarModelo()
			else:
				self.EntrenarModelo()
		else:
			self.EntrenarModelo()
		
		self.GuardarCambios()
		print self.Config._toString()	

	def AjustarConfig(self):
		if self.RutaEntrenamiento != "":
			self.Config.RT_ENTRENAMIENTO = self.RutaEntrenamiento
		if int(self.Iteraciones) > 0:
			self.Config.ITERACIONES_ENT = int(self.Iteraciones)
		if self.RutaSession != "":
			self.Config.RT_ESTADOSESSION = self.RutaSession

	def GuardarCambios(self):
		if self.GuardarXML == True:
			self.Config._guardarXML()

	def Prediccion(self):
		if ExisteArchivo(self.RutaTest):
			self.Prediccion = Prediccion(self.Config, self.RutaTest)
			resultados = self.Prediccion.Predecir()
			indice = int(resultados[0])
			print self.Datos.DT_Predicciones[indice]
		else:
			print "Ruta o archivo no existe en el sistema"
		
