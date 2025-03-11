# 10. Sprawdzenie różnicy wartości pikseli
#     a. Pobierz wartości pikseli w dwóch różnych miejscach obrazu i porównaj je
#     (np. (50,50) i (200,200) ).
#     b. Wypisz różnice w wartościach R, G, B.

import cv2
import numpy as np
image = cv2.imread('image.jpeg')

p1, p2 = image[50, 50], image[200, 200]
diff = np.abs(p1 - p2)
print(f'Difference: {diff}')