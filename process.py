import cv2
import numpy as np
from utils import *

def extraiDados(filestr):
  npimg = np.fromstring(filestr, np.uint8)

  img = cv2.imdecode(npimg, cv2.IMREAD_LOAD_GDAL)

  imglesao = img.copy()
  imgSegmentada =	segmenta(img)
  imglesaoSegmentada = segmenta(imglesao, lesao=True)

  imgfinal = preenche(imgSegmentada)
  imglesaofinal = preenche(imglesaoSegmentada)

  imgfinal = cv2.subtract(imgfinal, imglesaofinal)

  return {'areaLesao': calculaArea(imglesaofinal), 'areaSaudavel': calculaArea(imgfinal)}