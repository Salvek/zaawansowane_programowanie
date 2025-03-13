# Podstawowe przesunięcie
# a. Załaduj dowolny obraz i wyświetl go w oryginalnej postaci.
# b. Przesuń obraz o 30 pikseli w prawo i 40 pikseli w dół za pomocą macierzy
# transformacji M oraz cv2.warpAffine.
# c. Wyświetl wynik.

import cv2
import numpy as np
from util import *

image_path = 'C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg'

image = load_image(image_path)

show_image("Original", image)

M = np.float32([[1, 0, 30], [0, 1, 40]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

show_image("Shift", shifted)