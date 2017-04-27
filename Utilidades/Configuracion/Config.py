from Utilidades.Generales.Archivos import *
from lxml import etree

class Config:
	
	def __init__(self):
		self.ETI_CONTEO = 10
		self.ITERACIONES_ENT = 1000
		self.RT_ENTRENAMIENTO = CarpetaActual('Entrenamiento/')
		self.RT_ESTADOSESSION = CarpetaActual('Tensor/Modelo/Session/')
		self._getXML()

	def _getXML(self):
		if ExisteXML():
			doc = etree.parse(CarpetaActual('Utilidades/Configuracion/Config.xml'))
			self._getDataXML(doc)
		else:
			self._guardarXML()

	def _getDataXML(self,documento):
		raiz=documento.getroot()
		self._setCantidadEtiquetas(raiz.find("ETICONTEO").text)
		self._setIteracionesEntrenamiento(raiz.find("ITERACIONES").text)
		self._setRutaEntrenamiento(raiz.find("RUTAENTRENAMIENTO").text)
		self._setRutaEstadoSession(raiz.find("RUTASESSION").text)
	
	def _setCantidadEtiquetas(self,contEtiquetas):
		if contEtiquetas != "":
			self.ETI_CONTEO = contEtiquetas

	def _setIteracionesEntrenamiento(self,iteraciones):
		if iteraciones != "":
			self.ITERACIONES_ENT = iteraciones

	def _setRutaEntrenamiento(self,ruta):
		if ruta != "":
			self.RT_ENTRENAMIENTO = ruta

	def _setRutaEstadoSession(self,ruta):
		if ruta != "":
			self.RT_ESTADOSESSION = ruta

	def _guardarXML(self):
		newConfig=etree.Element("Config")
		doc=etree.ElementTree(newConfig)
		newConfig.append(etree.Element("ETICONTEO"))
		newConfig.append(etree.Element("ITERACIONES"))
		newConfig.append(etree.Element("RUTAENTRENAMIENTO"))
		newConfig.append(etree.Element("RUTASESSION"))
		newConfig[0].text=str(self.ETI_CONTEO)
		newConfig[1].text=str(self.ITERACIONES_ENT)
		newConfig[2].text=str(self.RT_ENTRENAMIENTO)
		newConfig[3].text=str(self.RT_ESTADOSESSION)
		GuardarXML('Utilidades/Configuracion/Config.xml',doc)
		

	def _toString(self):
		print 'Configuracion establecida'
		print 'Numero de Etiquetas = {}'.format(self.ETI_CONTEO)
		print 'Numero de Iteraciones = {}'.format(self.ITERACIONES_ENT)
		print 'Ruta de Entrenamiento = {}'.format(self.RT_ENTRENAMIENTO)
		print 'Ruta de Estado de Session TensorFlow = {}'.format(self.RT_ESTADOSESSION)
