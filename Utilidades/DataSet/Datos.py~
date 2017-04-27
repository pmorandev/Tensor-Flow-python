import numpy
from numpy import genfromtxt
from PIL import Image
from Utilidades.Generales.Archivos import LstImgEntrenamiento
from Utilidades.Configuracion.Config import Config

class DataSet:
	
	def __init__(self,config):
		self.Config = config
		self.list_imagenes = []
		self.list_etiquetas = []
		self.DT_Etiquetas = []
		self.DT_Imagenes = []
		self.DT_Predicciones = []

	def LeerArchivos(self):
		self.list_imagenes, self.list_etiquetas = LstImgEntrenamiento(self.Config.RT_ENTRENAMIENTO)
	
	def Cargar_Imagenes(self):
		for archivo in self.list_imagenes:
			imageFile = Image.open(archivo).convert(mode='L', dither=3)
			imageSize = imageFile.size
			rawData = imageFile.tobytes('raw')
			img = Image.frombytes('L', imageSize, rawData)
			patron = numpy.asarray(img, dtype="float") #.__xor__(1)
			
			
			for i in range(len(patron)):
				for j in range(len(patron[0])):
					if patron[i][j] == 255:
						patron[i][j] = 0.0
					elif patron[i][j] == 0:
						patron[i][j] = 1.0
					else:
						patron[i][j] = round((patron[i][j])/255, 1)

			vectorA=numpy.concatenate(patron)
			self.DT_Imagenes.append(vectorA)

	def Cargar_Etiquetas(self):
		vectorzero=[]
		rango = len(self.list_etiquetas)
		self.llenarVectorCero(vectorzero,rango)
		
		for i in range(rango):
			self.DT_Predicciones.append(self.list_etiquetas[i][0])
			for j in range(self.list_etiquetas[i][1]):
				self.llenarVectorCero(vectorzero,rango)
				vectorzero.insert(i,1)
				self.DT_Etiquetas.append(numpy.array(vectorzero))
		numpy.savetxt(self.Config.RT_ENTRENAMIENTO + 'Prediccion.csv', self.DT_Predicciones, delimiter=",",fmt='%s')

	def Cargar_Predicciones(self):
			self.DT_Predicciones=genfromtxt(self.Config.RT_ENTRENAMIENTO + 'Prediccion.csv', delimiter=',',dtype=None)

	def llenarVectorCero(self,vector,rango):
		del vector[:]
		for i in range(rango - 1):
		    vector.append(0)
		return vector
		
		
