# 8. Modyfikacja całego wiersza pikseli
#     a. Wczytaj obraz i zmień kolor wszystkich pikseli w 100. wierszu na zielony
#     (0, 255, 0) .
#     b. Wyświetl obraz przed i po zmianie.

import cv2
image = cv2.imread('image.jpeg')

modified_image = image.copy()
modified_image[100, :] = (0, 255, 0)
cv2.imshow("Before Modification", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("After Modification", modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()