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
            pixel = (img[i,j]**2)/255
            if(pixel > 255):
                img[i,j] = 255
            else:
                img[i,j] = pixel
           

    
    name, extension = os.path.splitext(filename)
    newname = "{name}-Quadratico{ext}".format(name=name,ext=extension)
    cv2.imshow('Quadratico', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(newname, img)
