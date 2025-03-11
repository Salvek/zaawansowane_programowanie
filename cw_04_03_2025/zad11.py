# 11. Znajdowanie najjaśniejszego piksela w obrazie
#     a. Przeszukaj cały obraz i znajdź piksel o najwyższej wartości jasności.
#     b. Wyświetl jego współrzędne i wartość.

import cv2
image = cv2.imread('image.jpeg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)
print(f'Brightest pixel at {max_loc} with value {max_val}')