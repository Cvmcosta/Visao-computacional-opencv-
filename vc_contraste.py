import numpy as np
import cv2
import os

def realce(filename, c, d):
    img = cv2.imread(filename, 0)

    rows, cols = img.shape
    print(rows)
    print(cols)


    for i in range(rows):
        for j in range (cols):
            img[i,j] = (img[i,j]-np.amin(img))*((d - c)/(np.amax(img) - np.amin(img)))+c

    print('acabou')
    
    name, extension = os.path.splitext(filename)
    newname = "{name}-Constraste{ext}".format(name=name,ext=extension)
    cv2.imshow('constraste', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(newname, img)
