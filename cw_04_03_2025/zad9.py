# 9. Zmiana wartości pikseli w określonym zakresie
#     a. Wypełnij obszar od (50,50) do (100,100) kolorem białym (255, 255, 255) .
#     b. Wyświetl obraz przed i po zmianie.

import cv2
image = cv2.imread('image.jpeg')

modified_image = image.copy()
modified_image[50:100, 50:100] = (255, 255, 255)
cv2.imshow("Before Modification", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("After Modification", modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()