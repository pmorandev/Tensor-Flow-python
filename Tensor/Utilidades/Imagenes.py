import numpy as nm
from PIL import Image,ImageFilter

def PrepararTest(ruta):

    csvImg = []
    im = Image.open(ruta).convert('L')
    width = float(im.size[0])
    height = float(im.size[1])
    newImage = Image.new('L', (28, 28), (255)) #creates white canvas of 28x28 pixels
    
    if width > height: #check which dimension is bigger
        nheight = int(round((20.0/width*height),0))
	print nheight
        if (nheight == 0): #rare case but minimum is 1 pixel
            nheight = 1  
        # resize and sharpen
        img = im.resize((20,nheight), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wtop = int(round(((28 - nheight)/2),0)) #caculate horizontal pozition
        newImage.paste(img, (4, wtop)) #paste resized image on white canvas
    else:
        #Height is bigger. Heigth becomes 20 pixels. 
        nwidth = int(round((20.0/height*width),0)) #resize width according to ratio height
        if (nwidth == 0): #rare case but minimum is 1 pixel
            nwidth = 1
         # resize and sharpen
        img = im.resize((nwidth,20), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wleft = int(round(((28 - nwidth)/2),0)) #caculate vertical pozition
        newImage.paste(img, (wleft, 4)) #paste resized image on white canvas
    
    tv = nm.array(newImage) #get pixel values

    for i in range(len(tv)):
			for j in range(len(tv[0])):
				if tv[i][j] > 200:
					tv[i][j] = 0
				else:
					tv[i][j] = 1

    print tv

    vectorA=nm.concatenate(tv)
    csvImg.append(vectorA)

    tva=nm.asarray(csvImg,dtype=nm.uint8)

    return tva

def PrepararImg(im):
	csvImg = []
	
	imageSize = im.size
	rawData = im.tobytes('raw')
	img = Image.frombytes('L', imageSize, rawData)
	patron = nm.asarray(img, dtype="float")

	puroCeros = True

	for i in range(len(patron)):
		for j in range(len(patron[0])):
			if patron[i][j] == 255:
				patron[i][j] = 0.0
			elif patron[i][j] == 0:
				puroCeros = False
				patron[i][j] = 1.0
			else:
				patron[i][j] = round((patron[i][j])/255, 1)

    	vectorA=nm.concatenate(patron)
    	csvImg.append(vectorA)

    	tva=nm.asarray(csvImg,dtype="float")
	if puroCeros == True:
		return []
	else:
    		return tva

def Lista28Img(ruta):
	lista_img = []
	imageFile = Image.open(ruta).convert(mode='L', dither=3)
	numW = int(round((imageFile.size[0])/28))
	numH = int(round((imageFile.size[1])/28))
	
	salto = 0
	for y in range(numH):
		salto = y * 28
		for i in range(numW):
			separacion = 28 * i
			imgCrop = imageFile.crop((separacion,salto,28 + separacion,28 + salto))
			arreglo = PrepararImg(imgCrop)
			if len(arreglo) > 0:
				lista_img.append(arreglo)	
	
	return lista_img
	'''
	rawData = imageFile.tobytes('raw')
	img = Image.frombytes('L', imageSize, rawData)
	patron = numpy.asarray(img, dtype="float") #.__xor__(1)
	'''
