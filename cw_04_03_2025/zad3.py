# 3. Znajdowanie środka obrazu
#     a. Wczytaj obraz i oblicz współrzędne jego środka.
#     b. Pobierz wartość koloru piksela w tym miejscu i wyświetl ją w konsoli.

import cv2
image = cv2.imread('image.jpeg')

h, w, _ = image.shape

x=h//2
y=w//2
(b, g, r) = image[x, y]
print("Pixel at ({}, {}) - Red: {}, Green: {}, Blue: {}".format(x, y, r, g, b))
