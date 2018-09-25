import numpy as np
import cv2
import os



#Para suavização de imagens
def detectar(filename, limiar):
    #Importa imagem
    img = cv2.imread(filename, 0)
    rows, cols = img.shape
    imgx = np.zeros((rows, cols))
    imgy = np.zeros((rows, cols))
    imgn = np.zeros((rows, cols))
    
    
    mascarax = np.matrix('1 0; 0 -1')
    mascaray = np.matrix('0 -1; 1 0')
    
    
    
    #cria mascara
    
    
    
    fator = 2//2
    
    
    for i in range(fator, rows-fator):
        for j in range(fator, cols-fator):
            soma = 0
            for f in range(2):
                for n in range(2):
                    soma = soma + (img[i+f-fator,j-fator+n]*mascarax[f,n])
            imgx[i,j] = soma
            
    for i in range(fator, rows-fator):
        for j in range(fator, cols-fator):
            soma1 = 0
            for f in range(2):
                for n in range(2):
                    soma1 = soma1 + (imgx[i+f-fator,j-fator+n]*mascaray[f,n])
            
   
            if(soma1<limiar):
                imgn[i,j]=0
            else:
                imgn[i,j]=255

    


    name, extension = os.path.splitext(filename)
    newname = "{name}-Roberts{ext}".format(name=name,ext=extension)
    cv2.imwrite(newname, imgn)
    cv2.imshow('Roberts',imgn)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
     
                        
