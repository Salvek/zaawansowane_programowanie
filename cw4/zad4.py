# Wykorzystanie funkcji imutils.translate
# a. Przesuń obraz o 50 pikseli w dół i 100 pikseli w prawo za pomocą
# imutils.translate .
# b. Porównaj wynik z przesunięciem wykonanym wcześniej przez cv2.warpAffine .
# Czy zauważyłeś różnice?

import cv2
import imutils

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
shifted = imutils.translate(image, 50, 100)
cv2.imshow("Shifted MYSZU", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()