# 5. Eksperymentowanie z pętlą
# a. Zmodyfikuj kod pętli rysującej okręgi, aby zamiast okręgów rysowała
# kwadraty. Każdy kolejny kwadrat powinien być większy o 20 pikseli od
# poprzedniego i mieć środek w tym samym miejscu.

import cv2
import numpy as np
from util import *

canvas = np.zeros((800, 800, 3), dtype="uint8")

h, w = canvas.shape[:2]

for r in range(0, 700, 20):
    cv2.rectangle(canvas, (h//2 - r, w//2 - r), (h//2 + r, w//2 + r), WHITE)

show_image("Loop", canvas)