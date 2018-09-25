# -*- coding: utf-8 -*-
"""
Feito por Pedropva em 28/08/2018
"""

import numpy as np
import cv2
import os,math, copy
import utils
import random



#detecção de pontos isolados
def pontos(img,limiar,filename):
    #fazendo o kernel
    kernel =[[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
    rows = img.shape[0]
    cols = img.shape[1]
    beirada = 3//2 #3 eh o numero delinhas da matriz
    valor = 0
    newImg = np.zeros((rows,cols))
    for i in range(beirada,rows-beirada):
        for j in range(beirada,cols-beirada):
            valor = 0
            for k in range(3):
                for l in range(3):
                    valor +=  img[i-beirada + k,j-beirada + l] * kernel[k][l] #multiplico os valores do kernel pela janela equivalente dos pixels
            
            if valor <= limiar:
                newImg[i,j] = 0
            else: 
                newImg[i,j] = 255      
            
    if filename != None:
        cv2.imwrite(filename,newImg)
        
    return newImg

#detecção de retas
def retas(img,angulo,limiar,filename):
    #fazendo o kernel
    if angulo == 0:
        kernel =[[-1,-1,-1],[2,2,2],[-1,-1,-1]]    
    elif angulo == 45:
        kernel =[[-1,-1,2],[-1,2,-1],[2,-1,-1]]    
    elif angulo == 90:
        kernel =[[-1,2,-1],[-1,2,-1],[-1,2,-1]]    
    elif angulo == -45:
        kernel =[[2,-1,-1],[-1,2,-1],[-1,-1,2]]    
    else:
        kernel =[[-1,-1,-1],[2,2,2],[-1,-1,-1]]    

    rows = img.shape[0]
    cols = img.shape[1]
    beirada = 3//2 #3 eh o numero delinhas da matriz
    valor = 0
    newImg = np.zeros((rows,cols))
    for i in range(beirada,rows-beirada):
        for j in range(beirada,cols-beirada):
            valor = 0
            for k in range(3):
                for l in range(3):
                    valor +=  img[i-beirada + k,j-beirada + l] * kernel[k][l] #multiplico os valores do kernel pela janela equivalente dos pixels            
            if valor <= limiar:
                newImg[i,j] = 0
            else: 
                newImg[i,j] = 255      
            
    if filename != None:
        cv2.imwrite(filename,newImg)
        
    return newImg

#detecção de retas
def roberts(img,limiar,filename):
    #fazendo o kernel
    kernelX =[[1,0],[0,-1]]
    kernelY =[[0,-1],[1,0]]

    rows = img.shape[0]
    cols = img.shape[1]
    beirada = 2//2 #2 eh o numero de linhas da matriz
    valorx = 0
    valorxy = 0
    imgX = np.zeros((rows,cols))
    imgXY = np.zeros((rows,cols))
    
    for i in range(beirada,rows-beirada):
        for j in range(beirada,cols-beirada):
            valorx = 0
            for k in range(2):
                for l in range(2):
                    valorx +=  img[i-beirada + k,j-beirada + l] * kernelX[k][l] #multiplico os valores do kernel pela janela equivalente dos pixels            
            imgX[i,j] = valorx
    #fim das convolucoes no eixo x, agora usa a saida disso pra fazer as convolucoes em y
    for i in range(beirada,rows-beirada):
        for j in range(beirada,cols-beirada):
            valorxy = 0
            for k in range(2):
                for l in range(2):
                    valorxy +=  imgX[i-beirada + k,j-beirada + l] * kernelY[k][l] #multiplico os valores do kernel pela janela equivalente dos pixels            
            #o valor xy ja eh o resultado as convolucoes em x e y
            if valorxy <= limiar:
                imgXY[i,j] = 0
            else: 
                imgXY[i,j] = 255      
            
    if filename != None:
        cv2.imwrite(filename,imgXY)
        
    return imgXY