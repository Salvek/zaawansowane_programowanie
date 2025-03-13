# 1. Rysowanie linii
# a. Narysuj niebieską linię od środka obrazu do jego prawego dolnego rogu.
# Grubość linii: 2 px.

import cv2
from util import *

image = cv2.imread(image_path)

h, w = image.shape[:2]

cv2.line(image, (w//2, h//2), (w, h), GREEN)
show_image("Line", image)