import numpy as np
import cv2
import os
#quantização code
def amostragem_process(img, n):
    amostra = [lin[::n] for lin in img[::n]]
    return np.array(amostra)

def amostragem(imgpath, fator):
    img = cv2.imread(imgpath, 0)
    amostra = amostragem_process(img, fator)
    name, extension = os.path.splitext(imgpath)
    newname = "{name}-amostragem-{ft}{ext}".format(name=name, ft=fator, ext=extension)
    cv2.imwrite(newname, amostra)
    img  = cv2.imread(newname,0)
    cv2.imshow(newname, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()