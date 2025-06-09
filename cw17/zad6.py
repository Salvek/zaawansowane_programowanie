import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
def nothing(x):
    pass

cv2.namedWindow("Progowanie Adaptacyjne", cv2.WINDOW_NORMAL)

cv2.createTrackbar("Wielkość Bloku", "Progowanie Adaptacyjne", 11, 51, nothing)  # Ustawienie maksymalnego na 51
cv2.createTrackbar("Wartość C", "Progowanie Adaptacyjne", 2, 20, nothing)

while True:
    block_size = cv2.getTrackbarPos("Wielkość Bloku", "Progowanie Adaptacyjne")
    c_value = cv2.getTrackbarPos("Wartość C", "Progowanie Adaptacyjne")

    if block_size % 2 == 0:
        block_size += 1
    if block_size < 3:
        block_size = 3

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, c_value)

    cv2.imshow("Progowanie Adaptacyjne", threshold_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()