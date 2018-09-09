import numpy as np
import cv2
import os
#quantização code
def quantizacao_process(img, k):
    a = np.float32(img)
    bucket = 256/k
    quantizado = (a/(256/k))
    return np.uint8(quantizado) *bucket

def quantizacao(imgpath, cores):
    img  = cv2.imread(imgpath,0)
    resultado = quantizacao_process(img, cores)
    name, extension = os.path.splitext(imgpath)
    newname = "{name}-quantizacao-{ft}{ext}".format(name=name, ft=cores, ext=extension)
    cv2.imwrite(newname, resultado)
    img  = cv2.imread(newname,0)
    cv2.imshow(newname, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()