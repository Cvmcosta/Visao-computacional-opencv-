import numpy as np
import cv2
import os


def vc_misturar(filename1,filename2,p1,p2):
    img1 = cv2.imread(filename1, 0)  
    img2 = cv2.imread(filename2, 0)

    
    if img1.shape[0] > img2 .shape[0]:
        rows, cols = img1.shape
    else:
        rows, cols = img2.shape

    img3 = np.zeros([rows,cols])
    for i in range(rows):
        for j in range(cols):
            img3[i,j] = (img1[i,j]*p1 + img2[i,j]*p2)/(p1+p2)
                
    #cria e mostra imagem nova
    name, extension = os.path.splitext(filename1)
    newname = "{name}-Mistura{ext}".format(name=name, ext=extension)  
    cv2.imwrite(newname,img3)
    img  = cv2.imread(newname,0)
    cv2.imshow(newname, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()