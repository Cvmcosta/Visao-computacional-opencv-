import numpy as np
import cv2
import os

def vc_translada(filename1,x,y):
    img1 = cv2.imread(filename1, 0)  
    rows, cols = img1.shape
    img3 = np.zeros([rows,cols])

    img3 = np.concatenate((img3,img3), axis=0)
    img3 = np.concatenate((img3,img3), axis=1)
    img3 = np.concatenate((img3,img3), axis=-1)
    img3 = np.concatenate((img3,img3), axis=0)
   
    
 
    for i in range(0,rows):
        for j in range(0,cols):
            mat =  [[1, 0,x],[0, 1,y],[0, 0, 1]]
            v = [] 
            v.append([i])
            v.append([j])
            v.append([1]) 
            v = multMat(mat,v)
            img3[v[0][0]+round(1.5*rows),v[1][0]+round(1.5*cols)] = img1[i,j]
            
    #cria e mostra imagem nova
    name, extension = os.path.splitext(filename1)
    newname = "{name}-Translada{ext}".format(name=name, ext=extension)  
    cv2.imwrite(newname,img3)
    img  = cv2.imread(newname,0)
    cv2.imshow(newname, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def multMat(m1, m2):
    matf = []
    for i in range(0,len(m1)):
        res = []
        for j in range(0,len(m2[0])):
            s = 0
            for k in range(0,len(m2)):  
                s += m1[i][k] * m2[k][j]
            res.append(s)
        matf.append(res)
    return matf