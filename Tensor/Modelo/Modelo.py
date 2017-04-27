import tensorflow as tf
from Tensor.Utilidades.Generales import *
from Utilidades.DataSet.Datos import DataSet

class Modelo:
	
	def __init__(self,Data):
		self.DataImg = Data.DT_Imagenes
		self.DataEtiqueta = Data.DT_Etiquetas
		self.Categorias = Data.Config.ETI_CONTEO
		self.Iteraciones = Data.Config.ITERACIONES_ENT
		self.RutaSession = Data.Config.RT_ESTADOSESSION
		self.Session = tf.InteractiveSession()
		self.y_ = tf.placeholder(tf.float32, [None, self.Categorias])
		self.x = tf.placeholder(tf.float32, [None, 784])
		self.keep_prob = 0.5
		self.y_conv = self.InitPesos()
		self.accuracy=self.Optimizacion()
		self.Entrenar()

	def InitPesos(self):
		self.W = tf.Variable(tf.zeros([784, self.Categorias]), name='W')
		self.b = tf.Variable(tf.zeros([self.Categorias]), name='b')
		y = tf.nn.softmax(tf.matmul(self.x, self.W) + self.b)

		W_conv1 = weight_variable([5, 5, 1, 32])
		b_conv1 = bias_variable([32])

		x_image = tf.reshape(self.x, [-1,28,28,1])
		h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
		h_pool1 = max_pool_2x2(h_conv1)

		W_conv2 = weight_variable([5, 5, 32, 64])
		b_conv2 = bias_variable([64])

		h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
		h_pool2 = max_pool_2x2(h_conv2)

		W_fc1 = weight_variable([7 * 7 * 64, 1024])
		b_fc1 = bias_variable([1024])

		h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
		h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

		self.keep_prob = tf.placeholder(tf.float32)
		h_fc1_drop = tf.nn.dropout(h_fc1, self.keep_prob)

		W_fc2 = weight_variable([1024, self.Categorias])
		b_fc2 = bias_variable([self.Categorias])

		return tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

	def Optimizacion(self):
		cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(self.y_conv, self.y_))
		self.train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
		correct_prediction = tf.equal(tf.argmax(self.y_conv,1), tf.argmax(self.y_,1))
	 	return tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

	def Entrenar(self):
		saver = tf.train.Saver(var_list={"W": self.W, "b": self.b})
		self.Session.run(tf.global_variables_initializer())

		for i in range(int(self.Iteraciones)):
			if i%100 == 0:
				train_accuracy = self.accuracy.eval(feed_dict={self.x:self.DataImg, self.y_: self.DataEtiqueta, self.keep_prob: 1.0})
	    			print("step %d, training accuracy %g"%(i, train_accuracy))
			self.train_step.run(feed_dict={self.x: self.DataImg, self.y_: self.DataEtiqueta, self.keep_prob: 0.5})

		saver.save(self.Session,self.RutaSession + "model.ckpt")
