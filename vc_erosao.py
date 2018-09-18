import numpy as np
import cv2
import os

def erosao(filename):
    img = cv2.imread(filename, 1)

    rows, cols = img.shape
    print(rows)
    print(cols)


    for i in range(rows):
        for j in range (cols):
            print("uau")

    
    name, extension = os.path.splitext(filename)
    newname = "{name}-Gama{ext}".format(name=name,ext=extension)
    cv2.imshow('gama', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(newname, img)
    