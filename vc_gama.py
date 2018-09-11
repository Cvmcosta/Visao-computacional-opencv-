import numpy as np
import cv2
import os

def realce(filename, c, gama):
    img = cv2.imread(filename, 0)

    rows, cols = img.shape
    print(rows)
    print(cols)


    for i in range(rows):
        for j in range (cols):
            value = c*(img[i,j]**gama)
            if(value>255):
                value = 255
            else:
                img[i,j] = value


    
    name, extension = os.path.splitext(filename)
    newname = "{name}-Gama{ext}".format(name=name,ext=extension)
    cv2.imshow('gama', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(newname, img)
    