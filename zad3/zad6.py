# 6. Zamazywanie szczegółów na zdjęciu
# a. Znajdź w Internecie profilowe zdjęcie osoby.
# b. Czerwonymi kołami “zasłoń” osobie na zdjęciu oczy.
# c. Zielonym prostokątem “zasłoń” osobie na zdjęciu usta.
# d. Niebieskim okręgiem obejmij dookoła twarz osoby.

import cv2
import numpy as np
from util import *

image = cv2.imread(image_path)

cv2.circle(image, (106, 86), 15, RED, 30)
cv2.circle(image, (170, 77), 15, RED, 30)
cv2.rectangle(image, (115, 122), (170, 156), GREEN, 5)
cv2.circle(image, (135, 99), 85, BLUE)
show_image("Face", image)