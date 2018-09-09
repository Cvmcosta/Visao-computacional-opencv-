import cv2
import numpy as np
import os



def sort(filename, newfilename, pos):
    img = cv2.imread(filename)

    img2 = np.zeros(((pos[2]-pos[0])+1,(pos[3]-pos[1])+1,3), dtype=np.uint8)
    
    iy = 0
    for i in range(pos[0],pos[2]):
        ix=0
        for j in range(pos[1],pos[3]):
            img2[ix, iy] = img[j,i]
            ix = ix+1
        iy=iy+1

    cv2.imshow('img2nova',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    ix = 0
    flag = 5
    for i in range(pos[0],pos[2]):
        if(flag>=5 and flag<10):
            img2[ix] = np.sort(img2[ix], axis=0)
        elif(flag>=10):
            flag=0
        flag = flag+1
        ix=ix+1




    #img2 = np.sort(img2, axis=0)    
    iy = 0
    for i in range(pos[0],pos[2]):
        ix=0
        for j in range(pos[1],pos[3]):
            img[j,i] = img2[ix, iy]
            ix = ix+1
        iy=iy+1       

    #cria e mostra imagem nova
      
    cv2.imwrite(newfilename,img)
    img  = cv2.imread(newfilename)
    cv2.imshow(newfilename, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

