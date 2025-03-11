# 6. Wypełnienie konkretnego obszaru obrazu jednolitym kolorem
#     a. Pobierz współrzędne środka obrazu.
#     b. Wypełnij kwadrat o wymiarach 100x100 px, którego środek pokrywa się ze
#     środkiem obrazu, kolorem czerwonym (0, 0, 255) .
#     c. Wyświetl obraz po zmianach.

import cv2
image = cv2.imread('image.jpeg')

h, w, _ = image.shape
center = (h//2, w//2)
x1, x2 = center[1] - 50, center[1] + 50
y1, y2 = center[0] - 50, center[0] + 50
image[y1:y2, x1:x2] = (0, 0, 255)
cv2.imshow("Modified Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()