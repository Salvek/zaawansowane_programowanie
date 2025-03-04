# Wczytaj i wyświetl obraz z podanej przez siebie ścieżki. Sprawdź, co się
# stanie, gdy podasz błędną ścieżkę.

import cv2
image = cv2.imread(image_path)

if image is None:
    print("Błąd: Nie udało się wczytać obrazu")
else:
    print("Obraz wczytano poprawnie.")

cv2.imshow("Wyświetlony obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()