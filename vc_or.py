import numpy as np
import cv2
import os



def or_imgs(filename1,filename2):
    img1 = cv2.imread(filename1, 0)  
    img2 = cv2.imread(filename2, 0)

    
    rows, cols = img1.shape
    img3 = np.zeros([rows,cols])
    for i in range(rows):
        for j in range(cols):
            img3[i,j] = 0
            if(img1[i, j] == 255 or img2[i, j] == 255):
                img3[i, j] = 255
    name, extension = os.path.splitext(filename1)
    
    newname = "{name}-Or{ext}".format(name=name, ext=extension)
    cv2.imwrite(newname, img3)
    img  = cv2.imread(newname,0)
    cv2.imshow(newname, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()