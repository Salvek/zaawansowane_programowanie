# Dynamiczne przesunięcie na podstawie parametrów użytkownika
# a. Zmodyfikuj kod, aby użytkownik mógł podać wartości przesunięcia tx i ty
# poprzez wprowadzenie ich z klawiatury (np. przy użyciu input())
# b. Sprawdź, jak działa przesunięcie dla różnych wartości.

import sys
import cv2
import imutils

shift_params = {"x": 0, "y": 0}
for key in shift_params.keys():
    try:
        shift_params[key] = int(input(f"Enter {key.upper()} shift parameter (int:\n"))
    except Exception:
        print(f"Invalid {key.upper()} parameter entered.\n")
        sys.exit()

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
shifted = imutils.translate(image, shift_params["x"], shift_params["y"])
cv2.imshow("Shifted MYSZU", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()