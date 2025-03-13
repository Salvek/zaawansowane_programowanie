# 2. Rysowanie prostokątów, utwórz czarny obraz o wymiarach 400x400 pikseli i
# narysuj na nim:
# a. Zielony prostokąt o wymiarach 100x50 pikseli w lewym górnym rogu.
# b. Czerwony prostokąt o grubości 3 px w prawym dolnym rogu.

import cv2
import numpy as np
from util import *

canvas = np.zeros((400, 400, 3), dtype="uint8")

cv2.rectangle(canvas, (0,0), (100, 50), GREEN)
cv2.rectangle(canvas, (400,400), (300, 350), RED, 3)

show_image("Rectangle", canvas)