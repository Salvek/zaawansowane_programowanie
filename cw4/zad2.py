# Przesunięcie w przeciwnym kierunku
# a. Wykorzystaj ten sam obraz co wcześniej.
# b. Przesuń go o 20 pikseli w lewo i 50 pikseli w górę.
# c. Wyświetl wynik.

import cv2
import numpy as np
from util import *

image_path = 'C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg'

image = load_image(image_path)

pd = np.float32([[1, 0, 30], [0, 1, 40]])
lg = np.float32([[1, 0, -20], [0, 1, -50]])

shifted = cv2.warpAffine(image, pd, (image.shape[1], image.shape[0]))
show_image("Shifted", shifted)

shifted = cv2.warpAffine(image, lg, (image.shape[1], image.shape[0]))

show_image("Shifted", shifted)