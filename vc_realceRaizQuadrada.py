import numpy as np
import cv2
import os

def realce(filename):
    img = cv2.imread(filename, 0)

    rows, cols = img.shape
    print(rows)
    print(cols)


    for i in range(rows):
        for j in range (cols):
            G = 255/np.sqrt(255)
            img[i,j] = G*(np.sqrt(img[i,j]))
        
    
    name, extension = os.path.splitext(filename)
    newname = "{name}-RaizQuadrada{ext}".format(name=name,ext=extension)
    cv2.imshow('Raiz Quadrada', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(newname, img)
