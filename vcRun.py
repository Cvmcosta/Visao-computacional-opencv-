import numpy as np
import cv2
import os
import vc_quantizacao
import vc_amostragem
import vc_and
import vc_or
import vc_not
import vc_AndNot
import vc_xor
import vc_add
import vc_sub
import vc_mult
import vc_div
import vc_dist
import vc_mistura
import vc_transladar
import vc_rotacao
import vc_escalar
import vc_pixelSort
import vc_faceDetect
import vc_channelShift
# Load an color image in grayscale

if __name__ == "__main__":
    filename = "imgs/big3.jpg"
    filename2 = "imgs/cat.jpg"
    fator = [4,8] #fator de amostragem
    cores = [2,8,16] #numero de cores da quantização
    names = []


    vc_faceDetect.detect(filename)

    """ img = cv2.imread(filename)
    
    for i in range(5):
        if(i%2==0):
            img = vc_channelShift.shift(img, 10, 0)
        else:
            img = vc_channelShift.shift(img, 10, 1)
        cv2.imshow('test',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    name, extension = os.path.splitext(filename)
    newname = "{name}-ChannelSHift{ext}".format(name=name, ext=extension)
    cv2.imwrite(newname, img) """