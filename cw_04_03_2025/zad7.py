# 7. Wycięcie fragmentu obrazu
#     a. Podziel obraz na 9 równych części.
#     b. Pobierz fragment obrazu obejmujący środek.
#     c. Wyświetl wycięty fragment osobno.

import cv2
image = cv2.imread('image.jpeg')

h, w, _ = image.shape
dx, dy = w//3, h//3
cropped = image[dy:2*dy, dx:2*dx]
cv2.imshow("Cropped Center", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()