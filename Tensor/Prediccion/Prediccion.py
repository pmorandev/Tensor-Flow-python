import tensorflow as tf
from Tensor.Utilidades.Generales import *
from Tensor.Utilidades.Imagenes import *

class Prediccion:
	def __init__(self,config,test):
		self.Config = config
		self.RutaTest = test

	def Predecir(self):
		x = tf.placeholder(tf.float32,[None,784])
		W=tf.Variable(tf.zeros([784,int(self.Config.ETI_CONTEO)]))
		b=tf.Variable(tf.zeros([int(self.Config.ETI_CONTEO)]))
		
		W_conv1=weight_variable([5,5,1,32])
		b_conv1=bias_variable([32])

		x_image=tf.reshape(x,[-1,28,28,1])
		h_conv1=tf.nn.relu(conv2d(x_image,W_conv1) + b_conv1)
		h_pool1=max_pool_2x2(h_conv1)

		W_conv2=weight_variable([5,5,32,64])
		b_conv2=bias_variable([64])

		h_conv2=tf.nn.relu(conv2d(h_pool1,W_conv2) + b_conv2)
		h_pool2=max_pool_2x2(h_conv2)

		W_fc1=weight_variable([7*7*64,1024])
		b_fc1=bias_variable([1024])

		h_pool2_flat=tf.reshape(h_pool2,[-1,7*7*64])
		h_fc1=tf.nn.relu(tf.matmul(h_pool2_flat,W_fc1) + b_fc1)

		keep_prob=tf.placeholder(tf.float32)
		h_fc1_drop=tf.nn.dropout(h_fc1,keep_prob)

		W_fc2=weight_variable([1024,int(self.Config.ETI_CONTEO)])
		b_fc2=bias_variable([int(self.Config.ETI_CONTEO)])

		y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop,W_fc2) + b_fc2)

		init_op = tf.global_variables_initializer()

		saver = tf.train.Saver(var_list={"W": W, "b": b})

		with tf.Session() as sess:
				image_contents = tf.read_file(self.RutaTest)
				image = tf.image.decode_jpeg(image_contents, channels=3)
				#image = tf.image.rgb_to_grayscale(image, name=None)
				sess.run(init_op)
				saver.restore(sess,self.Config.RT_ESTADOSESSION + 'model.ckpt')
		   
				prediction=tf.argmax(y_conv,1)
				
				tva=PrepararTest(self.RutaTest)

				return prediction.eval(feed_dict={x: tva,keep_prob:1.0}, session=sess)
'''
		try:
			with tf.Session() as sess:
				image_contents = tf.read_file(self.RutaTest)
				image = tf.image.decode_jpeg(image_contents, channels=3)
				image = tf.image.rgb_to_grayscale(image, name=None)
				sess.run(init_op)
				#tmp = sess.run([image])
				saver.restore(sess,self.Config.RT_ESTADOSESSION + 'model.ckpt')
		   
				prediction=tf.argmax(y_conv,1)
				return prediction.eval(feed_dict={x: [image],keep_prob:1.0}, session=sess)
		except:
			pass
'''
'''
			resultados = []
			for i in range(len(imgData)):
				resultados.append(prediction.eval(feed_dict={x: imgData[i],keep_prob:1.0}, session=sess))
			
		return resultados
'''
