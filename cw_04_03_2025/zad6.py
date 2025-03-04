# Zmień rozmiar okna wyświetlania obrazu tak, by dostosować je do różnych
# ekranów, np. cv2.WINDOW_NORMAL - znajdź w dokumentacji odpowiednią funkcję
# do tego.

import cv2
image = cv2.imread(image_path)

if image is None:
    print('Nie można wczytać obrazu')

cv2.namedWindow("Obraz", cv2.WINDOW_NORMAL)
cv2.imshow('Obraz', image)
cv2.waitKey(0)
cv2.destroyAllWindows()