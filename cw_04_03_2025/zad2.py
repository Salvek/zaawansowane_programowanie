# 2. Modyfikacja pojedynczego piksela
#     a. Zmień kolor piksela w prawym dolnym rogu obrazu na czerwony (0, 0, 255) .
#     b. Wyświetl obraz przed i po zmianie.

import cv2
image = cv2.imread('image.jpeg')

modified_image = image.copy()
h, w, _ = modified_image.shape
modified_image[h-1, w-1] = (0, 0, 255)

x=h-1
y=w-1
(b, g, r) = image[x, y]
print("Pixel at ({}, {}) (Before mod) - Red: {}, Green: {}, Blue: {}".format(x, y, r, g, b))
image[x, y] = (0, 0, 255)
(b, g, r) = modified_image[x, y]
print("Pixel at ({}, {}) (After mod) - Red: {}, Green: {}, Blue: {}".format(x, y, r, g, b))

cv2.imshow("Obraz", image)
cv2.imshow("Obraz zmodyfikowany", modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()