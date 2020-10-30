import cv2
import numpy as np

img= cv2.imread('venom.jpg')
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

def Blanco_y_Negro(A):
    filas= A.shape[0]
    cols= A.shape[1]
    B= np.zeros((filas,cols),np.float32)
    for row in range(filas):
        for col in range(cols):
            for color in range(len(A[row][col])):
                B[row][col]+= A[row][col][color]
            B[row][col]= B[row][col]/3
            if B[row][col] > 127: 
                B[row][col]= 255
            else:
                B[row][col]= 0
    return B

nueva= Blanco_y_Negro(img)
nueva= cv2.cvtColor(nueva,cv2.COLOR_GRAY2RGB)
cv2.imwrite('ImagenByN.jpg',nueva)
