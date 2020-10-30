import cv2
import nunmy as np

img = cv2.imread('venom.jpg')

def convolucionPadding (A, B):
    C = np.zeros (len(A), len(A[0])
    for row in range (0, len(A)):
        for col in range (0, len(A[0]):
            sum = 0
            for x in range (0, len(B)):
                for y in range (0, len(B[0]):
                    suma += A[row + x][col + y]*B[x][y]
            C[row][col] = suma
    return C
    
    
   
def convolucion (X, Y):
    Z = np.zeros((len(X)-2,len(X[0])-2),np.float32)
    for row in range(0,len(X)-2):
        for col in range(0,len(X[row])-2):
            Z[row][col] = X[row][col]*Y[0][0] + X[row][col+1]*Y[0][1] + X[row][col+2]*Y[0][2] + X[row+1][col]*Y[1][0] + X[row+1][col+1]*Y[1][1] + X[row+1][col+2]*Y[1][2] + X[row+2][col]*Y[2][0] + X[row+2][col+1]*Y[2][1] + X[row+2][col+2]*Y[2][2]       
    return Z
    
    
    

NuevaImg = convolucionPadding(img)
Filtro1 = [[1,1,1],[1,0,1],[1,1,1]]

final = convolucion(NuevaImg, Filtro1)

cv2.imwrite("ImagenConPadding.jpg",final)
