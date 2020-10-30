import cv2
import numpy as np

img= cv2.imread('venom.jpg')
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

def EscalaDeGrises(A):
    filas= A.shape[0]
    cols= A.shape[1]
    B= np.zeros((filas,cols),np.float32)
    for row in range(filas):
        for col in range(cols):
            for color in range(len(A[row][col])):
                B[row][col]+= A[row][col][color]
            B[row][col]= B[row][col]/3
    return B

def CrearPadding(A):
    filas= A.shape[0]
    cols=A.shape[1]
    matriz= np.zeros((filas+2,cols+2),np.float32)
    for row in range(1,filas+1):
        for col in range(1,cols+1):
            matriz[row][col]= A[row-1][col-1]
    return matriz

def convolucion(A,B):
    C= np.zeros((len(A)-2,len(A[0])-2),np.float32)
    for row in range(0,len(A)-2):
        for col in range(0,len(A[row])-2):
            C[row][col]=A[row][col]*B[0][0]+A[row][col+1]*B[0][1]+A[row][col+2]*B[0][2]+A[row+1][col]*B[1][0]+A[row+1][col+1]*B[1][1]+A[row+1][col+2]*B[1][2]+A[row+2][col]*B[2][0]+A[row+2][col+1]*B[2][1]+A[row+2][col+2]*B[2][2]
	    
    return C


nueva= EscalaDeGrises(img)
filtro= [[1,1,1],[1,0,1],[1,1,1]]
ConPadding= CrearPadding(nueva)

final=convolucion(ConPadding,filtro)
final= cv2.cvtColor(final,cv2.COLOR_GRAY2RGB)

print("Dimensiones: \n")
print(final.shape)
cv2.imwrite("ImagenConP.jpg",final)
