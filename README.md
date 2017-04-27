# Tensor-Flow-python
Programa de entrenamiento configurable para reconocimiento de patrones (letras, numeros, simbolos etc.) con TensorFlow

Este es un pequeño programa que por linea de comandos recibe una serie de argumentos para realizar las tareas de entrenamiento y
reconicimiento de patrones.

El programa al iniciar valida una serie de condiciones por ejemplo si existe archivos de estado del Tensor entrenado, si no ay un archivo
de estado este entiende que se tiene que entrenar el tensor con una serie de imagenes separadas por carpetas donde cada carpeta corresponde
al patron que se quiere entrenar el tensor para su reconocimiento.

Al igual el programa guarda en un archivo xml su configuracion previa como ser la ruta donde se encuentra las imagenes a entrenar,
la ruta donde se encuentra guardada los estados del tensor entrenado. Tambien cuenta con el numero de etiquetas a identificar y
el numero de iteraciones para el entrenamiento (Este es importante ya que a mayores iteraciones mayor es el porcentaje de prediccion del
programa).

Los parametros que recibe el programa son:

 * -a, --ayuda     : Esto desplegara en la terminal una pequeña guia de los significados de los comandos recibidos.
 * -g, --guadar    : Guarda en el archivo xml del programa las opciones ingresadas.
 * -e, --entrenar  : Comando que indica que el Tensor se entrenara de nuevo con las rutas de entrenamientos dadas o por las default del 
                    sistema.
 * -i,--intervalos : Cantidad de iteraciones que hara el sistema al entrenar el Tensor.
 * -t,--test       : Ruta del archivo que el Tensor tratara de identificar de acuerdo a su entrenamiento 
                  (Solo se aceptan formatos de imagenes).
 * -r,--rutaimg    : Ruta donde se encuentran las imagenes para el entrenamiento del Tensor (En caso de no darse esta opcion el sistema
                  acudira a la ruta default dada ya al programa)
 * -s,--sessionruta: Ruta donde se guardara los estados del Tensor entrenado (En caso de no darse esta opcion el sistema acudira a la ruta
                  default dada ya al programa)
                  
Algunas obseraciones dadas es que las imagenes de entrenamiento tienen que ser de dimensiones 25 x 25 en cualquier formato valido de
imagen. Las etiquetas que identificara el sistema seran tomadas de los nombres de las carpetas de las imagenes de entrenamiento, 
por ejemplo, si en la carpeta de entrenamiento contiene una sbcarpeta llamada circulo el sistema entendera que todo patron que identifique
con las imagenes dentro de esa carpeta seran llamadas circulo.

Las librerias utilizadas por el sistema son:
  * sys
  * getopt
  * lxml
  * os
  * re
  * numpy
  * PIL
  * tensorflow
  
Para mas informacion sobre Tensor Flow puede visitar la pagina oficial del proyecto https://www.tensorflow.org/
