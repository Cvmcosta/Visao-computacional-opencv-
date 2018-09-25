import numpy as np
import cv2
import os



#Para suavização de imagens
def aplicarFiltro(filename):
    #Importa imagem
    img = cv2.imread(filename, 0)
    rows, cols = img.shape
    img2 = np.zeros((rows, cols), np.uint8)
    #cria mascara
    mascara = np.matrix('1 2 1; 2 4 2; 1 2 1')
    
    fator = 3
    
    
    for i in range(rows):
        for j in range(cols):
            soma = 0
            if(i+fator-1<rows and j+fator-1<cols):
                for f in range(fator):
                    for n in range(fator):
                        soma = soma + (img[i+f,j+n]*mascara[f,n])
              
                img2[(int)(i+((fator-1)/2)), (int)(j+((fator-1)/2))] = soma/16

    name, extension = os.path.splitext(filename)
    newname = "{name}-FiltroGaussiano{ext}".format(name=name,ext=extension)
    cv2.imwrite(newname, img2)
   
    cv2.destroyAllWindows()
    return newname
     
                        
