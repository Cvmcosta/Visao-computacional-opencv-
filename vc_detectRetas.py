import numpy as np
import cv2
import os



#Para suavização de imagens
def detectar(filename, limiar, ang):
    #Importa imagem
    img = cv2.imread(filename, 0)
    rows, cols = img.shape
    imgx = np.zeros((rows, cols), np.uint8)
    
    if(ang == 0):
        mascara = np.matrix('-1 -1 -1; 2 2 2; -1 -1 -1')
    elif(ang == 45):
        mascara = np.matrix('-1 -1 2; -1 2 -1; 2 -1 -1')
    elif(ang == -45):
        mascara = np.matrix('2 -1 -1; -1 2 -1; -1 -1 2')
    elif(ang == 90):
        mascara = np.matrix('-1 2 -1; -1 2 -1; -1 2 -1')
    else:
        mascara = np.matrix('-1 -1 -1; 2 2 2; -1 -1 -1')
    
    #cria mascara
    
    
    
    fator = 3
    
    
    for i in range(fator-2, rows-fator-2):
        for j in range(fator-2, cols-fator-2):
            soma = 0
            for f in range(fator):
                for n in range(fator):
                    soma = soma + (img[i+f-1,j+n-1]*mascara[f,n])
            if(soma>limiar):
                imgx[i,j]=255
            else:
                 imgx[i,j]=0
   




    #newname = "{name}-FiltroGaussiano{ext}".format(name=name,ext=extension)
    #cv2.imwrite(newname, imx1)
    cv2.imshow('Retas',imgx)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
     
                        
