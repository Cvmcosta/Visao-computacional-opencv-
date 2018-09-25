import numpy as np
import cv2
import os



#Para suavização de imagens
def detectar(filename, limiar):
    #Importa imagem
    img = cv2.imread(filename, 0)
    rows, cols = img.shape
    imgx = np.zeros((rows, cols), np.uint8)
    
    
    #cria mascara
    mascara = np.matrix('-1 -1 -1; -1 8 -1; -1 -1 -1')
    
    
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
    cv2.imshow('Pontos',imgx)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
     
                        
