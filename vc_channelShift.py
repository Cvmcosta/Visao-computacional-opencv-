import numpy as np
import cv2
import os

def shift(img, factor, axis):
   
    b,g,r = cv2.split(img)

    rows, cols, color = img.shape

    if(axis==0):
        for i in range(rows):
            for j in range(cols):
                if(j+factor<cols):
                    img[i,j+factor][2] = r[i,j]
            
        for i in range(rows):
            for j in range(cols):
                if(j+factor*2<cols):
                    img[i,j+factor*2][1] = g[i,j]
                
        for i in range(rows):
            for j in range(cols):
                if(j+factor*3<cols):
                    img[i,j+factor*3][0] = b[i,j]
    elif(axis==1):
        for i in range(rows):
            for j in range(cols):
                if(i+factor<rows):
                    img[i+factor,j][2] = r[i,j]
            
        for i in range(rows):
            for j in range(cols):
                if(i+factor*2<rows):
                    img[i+factor*2,j][1] = g[i,j]   

        for i in range(rows):
            for j in range(cols):
                if(i+factor*3<rows):
                    img[i+factor*3,j][0] = b[i,j]
              
    return img

def createImg(filename, pos, factor, axis):
    img = cv2.imread(filename)

    img2 = np.zeros(((pos[2]-pos[0])+1,(pos[3]-pos[1])+1,3), dtype=np.uint8)
    
    iy = 0
    
   
    for i in range(pos[0],pos[2]):
        ix=0
        for j in range(pos[1],pos[3]):
        
            img2[ix, iy] = img[j,i]
            ix = ix+1
        
        iy=iy+1

    img2 =  shift(img2, factor, axis)

    iy = 0
    for i in range(pos[0],pos[2]):
        ix=0
        for j in range(pos[1],pos[3]):
            img[j,i] = img2[ix, iy]
            ix = ix+1
        iy=iy+1       
    
    return img