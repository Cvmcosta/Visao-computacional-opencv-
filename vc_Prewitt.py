import numpy as np
import cv2
import os



#Para suavização de imagens
def detectar(filename):
    #Importa imagem
    img = cv2.imread(filename, 0)
    rows, cols = img.shape
    imgx = np.zeros((rows, cols), np.uint8)
    imgy = np.zeros((rows, cols), np.uint8)
    imgn = np.full((rows,cols), 255)
    #cria mascara
    mascarax = np.matrix('-1 -1 -1; 0 0 0; -1 -1 -1')
    mascaray = np.matrix('-1 0 1;-1 0 1; -1 0 1')
    
    fator = 3
    
    
    for i in range(rows):
        for j in range(cols):
            soma = 0
            if(i+fator-1<rows and j+fator-1<cols):
                for f in range(fator):
                    for n in range(fator):
                        soma = soma + (img[i+f,j+n]*mascarax[f,n])
              
                imgx[i,j] = soma/3
    for i in range(rows):
        for j in range(cols):
            soma = 0
            if(i+fator-1<rows and j+fator-1<cols):
                for f in range(fator):
                    for n in range(fator):
                        soma = soma + (img[i+f,j+n]*mascaray[f,n])
              
                imgy[i,j] = soma/3
    
     
    for i in range(rows):
        for j in range(cols):
          
            value = imgx[i,j] + imgy[i,j]
            print( value)
            if(value>255):
                value=255
            imgn[i,j] = value
            
              


    name, extension = os.path.splitext(filename)



    #newname = "{name}-FiltroGaussiano{ext}".format(name=name,ext=extension)
    #cv2.imwrite(newname, imx1)
    cv2.imshow('x',imgx)
    cv2.waitKey(0)
    cv2.imshow('y',imgy)
    cv2.waitKey(0)
    cv2.imshow('t',imgn)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
     
                        
