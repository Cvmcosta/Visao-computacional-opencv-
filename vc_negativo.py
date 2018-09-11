import numpy as np
import cv2
import os

def negativa(filename):
    img = cv2.imread(filename, 0)

    rows, cols = img.shape

    img = img/255

    for i in range(rows):
        for j in range (cols):
            img[i,j] = 255 - img[i,j]

    img = img*255

    name, extension = os.path.splitext(filename)
    newname = "{name}-Negativo{ext}".format(name=name,ext=extension)
    cv2.imshow('negativado', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(newname, img)