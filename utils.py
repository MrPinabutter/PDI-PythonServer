import cv2
import numpy as np

def preenche(img):
	imgfloodfill = img.copy()
	h, w = img.shape[:2]
	mask = np.zeros((h+2, w+2), np.uint8)
	cv2.floodFill(imgfloodfill, mask, (0,0), 255);
	imgInvertida = cv2.bitwise_not(imgfloodfill)
	imgFinal = img | imgInvertida
	return imgFinal

def redimensiona(img, escala=40):
    escala = escala
    largura = int(img.shape[1] * escala/100)
    altura = int(img.shape[0] * escala/100)
    dim = (largura, altura)
    # resize image
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return img

def segmenta(img, lesao=False):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    if lesao == False:
        tomClaro = np.array([40, 100, 100])
        tomEscuro = np.array([80, 255, 255])
    else:
        #lesao:
        #242, 5, 5  239, 0, 21
        tomClaro = np.array([160, 100, 100])
        tomEscuro = np.array([200, 255, 255])
    
    imgSegmentada =	cv2.inRange(imgHSV, tomClaro, tomEscuro)
    # if lesao==True: 
    #     cv2.imshow("Original", imgSegmentada)	
    return imgSegmentada

def trataRuido(img):
    elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    img =	cv2.erode(img, elementoEstruturante, iterations = 6)
    return img

def calculaArea(img):
    #Obtendo os	contornos dos objetos na imagem
    modo = cv2.RETR_TREE;
    metodo = cv2.CHAIN_APPROX_SIMPLE;
    contornos, hierarquia = cv2.findContours(img,	modo, metodo)
    #Obtendo os	contornos do primeiro objeto segmentado
    objeto = contornos[0]
    #Obtendo a área do objeto segmentado
    area = cv2.contourArea(objeto)
    return area