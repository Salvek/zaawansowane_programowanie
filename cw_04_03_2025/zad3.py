# Wczytaj zdjęcie w odcieniach szarości i wyświetl liczbę kanałów.

import cv2

image = cv2.imread(image_path)
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

(h, w, c) = image_gray.shape
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f'channels: {c}')

# cv2.imshow("Wyświetlony obraz", image_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()