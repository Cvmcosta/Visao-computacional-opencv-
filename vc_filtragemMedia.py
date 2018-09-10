import numpy as np
import cv2
import os



#Para suavização de imagens
def aplicarFiltro(filename, fator):
    #Importa imagem
    img = cv2.imread(filename, 0)
    rows, cols = img.shape
    img2 = np.zeros((rows, cols), np.uint8)
    #cria mascara
    mascara  = np.zeros((fator,fator), np.uint8)+1
    
    
    for i in range(rows):
        for j in range(cols):
            soma = 0
            if(i+fator-1<rows and j+fator-1<cols):
                for f in range(fator):
                    for n in range(fator):
                        soma = soma + (img[i+f,j+n]*mascara[f,n])
              
                img2[(int)(i+((fator-1)/2)), (int)(j+((fator-1)/2))] = soma/(fator*fator)

    name, extension = os.path.splitext(filename)
    newname = "{name}-FiltroMedio{fator}{ext}".format(name=name, fator=fator,ext=extension)
    cv2.imwrite(newname, img2)
    cv2.imshow(newname,img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
     
                        
