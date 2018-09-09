import numpy as np
import cv2
import vc_pixelSort
import os


def detect(filename):
    face_cascade = cv2.CascadeClassifier('/home/cvm/anaconda3/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
    img = cv2.imread(filename)
    imgb = cv2.imread(filename)


    name, extension = os.path.splitext(filename)
    newfilename = "{name}-DataMosh{ext}".format(name=name, ext=extension)


    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        pos=[x, y, w+x, y+h]
        cv2.imshow('img',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        img2 = np.zeros(((pos[2]-pos[0])+1,(pos[3]-pos[1])+1,3), dtype=np.uint8)
        iy = 0
        for i in range(pos[0],pos[2]):
            ix=0
            
            for j in range(pos[1],pos[3]):
                img2[ix, iy] = imgb[j,i]
                ix = ix+1
            iy=iy+1
        gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 3)
        for (x,y,w,h) in faces:
            
            cv2.rectangle(img2,(x,y),(x+w,y+h),(255,0,0),2)
            array=[pos[0]+x, pos[1]+y, pos[0]+w+x, pos[1]+y+h]
        cv2.imshow('img2',img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        vc_pixelSort.sort(filename, newfilename,array)
        filename = newfilename