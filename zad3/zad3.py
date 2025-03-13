# 3. Rysowanie okręgów, utwórz czarny obraz o wymiarach 300x300 pikseli i
# narysuj na nim:
# a. Niebieski okrąg o promieniu 40 px w lewym górnym rogu.
# b. Czerwony okrąg o promieniu 60 px w środku obrazu.

import cv2
import numpy as np
from util import *

canvas = np.zeros((300, 300, 3), dtype="uint8")

h, w = canvas.shape[:2]

cv2.circle(canvas, (30, 30), 30, BLUE)
cv2.circle(canvas, (h//2, w//2), 40, GREEN)

show_image("Rectangle", canvas)