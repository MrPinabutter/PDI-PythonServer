import cv2
from utils import *

def extraiDados(imgPath):
  img = cv2.imread(imgPath)
  img = redimensiona(img, escala=40)

  imglesao = img.copy()

  imgSegmentada =	segmenta(img)
  imglesaoSegmentada = segmenta(imglesao, lesao=True)

  imgfinal = preenche(imgSegmentada)
  imglesaofinal = preenche(imglesaoSegmentada)

  imgfinal = cv2.subtract(imgfinal, imglesaofinal)
  cv2.destroyAllWindows()

  return {'areaLesao': calculaArea(imglesaofinal), 'areaSaudavel': calculaArea(imgfinal)}