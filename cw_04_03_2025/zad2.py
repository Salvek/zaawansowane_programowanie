# Wczytaj zdjęcie w kolorze i wyświetl liczbę kanałów.

import cv2

image = cv2.imread(image_path)

(h, w, c) = image.shape
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f'channels: {c}')

cv2.imshow("Wyświetlony obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()