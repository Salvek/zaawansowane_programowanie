# Otwórz dwa obrazy jednocześnie w osobnych oknach. Upewnij się, że można
# je zamknąć niezależnie.

import cv2

image1 = cv2.imread(image_path)
image2 = cv2.imread(image_path2)

if image1 is None or image2 is None:
    print("Błąd: Nie udało się wczytać obrazu")


cv2.imshow("Wyświetlony obraz 1", image1)
cv2.imshow("Wyświetlony obraz 2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

