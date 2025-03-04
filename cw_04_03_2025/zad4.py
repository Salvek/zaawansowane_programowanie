# Wczytaj obraz w skali szarości i zapisz go jako nowy plik - znajdź w
# dokumentacji odpowiednią funkcję do tego.

import cv2
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image_gray is None:
    print("Błąd: Nie udało się wczytać obrazu")
else:
    print("Obraz wczytano poprawnie.")

image_gray = cv2.imwrite(output_path, image_gray)
print(f"Obraz zapisano jako {output_path}")
