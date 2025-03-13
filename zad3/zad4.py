# 4. Złożona figura
# a. Narysuj na obrazie figurę składającą się z kwadratu o wymiarach 100x100
# px, wewnątrz którego znajduje się mniejszy okrąg o promieniu 30 px.
# Wszystko powinno być wycentrowane na obrazie.

import cv2
import numpy as np
from util import *

canvas = np.zeros((700, 700, 3), dtype="uint8")

h, w = canvas.shape[:2]

cv2.rectangle(canvas, (h//2 - 50, w//2 - 50), (h//2 + 50, w//2 + 50), RED, 3)
cv2.circle(canvas, (h//2, w//2), 30, GREEN)

show_image("Circle", canvas)