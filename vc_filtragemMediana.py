import numpy as np
import cv2
import os


def aplicarFiltro(filename, matSize):
    #Importa imagem
    img = cv2.imread(filename, 0)
    rows, cols = img.shape
    img2 = np.zeros((rows, cols), np.uint8)
    
    edge = matSize//2

    for i in range(edge, rows-edge):
        for j in range(edge, cols-edge):
            pixels = []
            for k in range(matSize):
                for l in range(matSize):
                    pixels.append(img[i - edge + k,j - edge + l])                    
            img2[i,j] = np.median(pixels)
    
    
    name, extension = os.path.splitext(filename)
    newname = "{name}-Mediana{ext}".format(name=name,ext=extension)
    cv2.imshow('Mediana', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(newname, img)
    