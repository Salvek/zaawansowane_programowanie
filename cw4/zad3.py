# Eksperymentowanie z dużymi wartościami przesunięcia
# a. Przesuń obraz o więcej niż połowę jego szerokości i wysokości.
# b. Sprawdź, co dzieje się z pikselami, które wychodzą poza zakres
# oryginalnego obrazu.

import cv2
import numpy as np
from util import *

image_path = 'C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg'

image = load_image(image_path) 

h, w = image.shape[:2]

S = np.float32([[1, 0, 150], [0, 1, 200]])

shifted = cv2.warpAffine(image, S, (image.shape[1], image.shape[0]))
show_image("Shifted", shifted)