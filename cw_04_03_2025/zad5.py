# 5. Kolorowanie fragmentu obrazu
#     a. Podziel obraz na 4 równe części (ćwiartki).
#     b. Wypełnij lewą górną ćwiartkę kolorem niebieskim (255, 0, 0) .
#     c. Wyświetl obraz po zmianach.
import cv2
image = cv2.imread('image.jpeg')

h, w, _ = image.shape

modified_image = image.copy()
modified_image[:h//2, :w//2] = (255, 0, 0)
cv2.imshow("Modified Image", modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()