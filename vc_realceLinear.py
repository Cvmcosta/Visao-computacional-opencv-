import numpy as np
import cv2
import os

def realce(filename, G, D):
    img = cv2.imread(filename, 0)

    rows, cols = img.shape
    print(rows)
    print(cols)


    for i in range(rows):
        for j in range (cols):
            pixel = G*img[i,j] + D
            if(pixel > 255):
                img[i,j] = 255
            else:
                img[i,j] = pixel
           

    
    name, extension = os.path.splitext(filename)
    newname = "{name}-Linear{ext}".format(name=name,ext=extension)
    cv2.imshow('Linear', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(newname, img)
