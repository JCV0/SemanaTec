import cv2
import numpy as np
def escala_grises():

	imagen=cv2.imread("venom.jpg")
	imagenh=imagen.shape[0]
	imagenw=imagen.shape[1]
	Matriz=np.zeros((imagenh,imagenw),np.uint8)
	im2=np.int16(imagen)
	for i in range(imagenh):
		for j in range(imagenw):
			Matriz[i,j]=(im2[i,j,2]+im2[i,j,1]+im2[i,j,0])/3


	cv2.imshow("imagen",imagen)
	cv2.imshow("imagegn",Matriz)
	cv2.waitKey(0)
escala_grises()
