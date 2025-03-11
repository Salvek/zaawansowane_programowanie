# 1. Odczyt wartości piksela
#     a. Wczytaj obraz i pobierz wartość piksela znajdującego się w lewym górnym
#     rogu (współrzędne 0,0 ).
#     b. Wyświetl wartości składowych koloru (R, G, B).

import cv2
image = cv2.imread('image.jpeg')

x=0
y=0
(b, g, r) = image[x, y]
print("Pixel at ({}, {}) - Red: {}, Green: {}, Blue: {}".format(x, y, r, g, b))