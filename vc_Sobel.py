import numpy as np
import cv2
import os



#Para suavização de imagens
def detectar(filename, limiar):
    #Importa imagem
    img = cv2.imread(filename, 0)
    rows, cols = img.shape
  
    imgn = np.zeros((rows, cols))
    
    
    mascarax = np.matrix('-1 0 1; -2 0 2; -1 0 1')
    mascaray = np.matrix('-1 -2 -1;0 0 0; 1 2 1')
    
    
    
    #cria mascara
    
    
    
    fator = 3//2
    
    
    for i in range(fator, rows-fator):
        for j in range(fator, cols-fator):
            soma = 0
            soma1 = 0
            for f in range(3):
                for n in range(3):
                    soma = soma + (img[i+f-fator,j-fator+n]*mascarax[f,n])
                    soma1 = soma1 + (img[i+f-fator,j-fator+n]*mascaray[f,n])
            if(abs(soma)+abs(soma1)<limiar):
                imgn[i,j]=0
            else:
                imgn[i,j]=255
           
   
   
    


    name, extension = os.path.splitext(filename)
    newname = "{name}-Sobel{ext}".format(name=name,ext=extension)
    cv2.imwrite(newname, imgn)
    cv2.imshow('Sobel',imgn)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
     
                        
