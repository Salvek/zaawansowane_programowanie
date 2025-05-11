import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([75, 75, 75])
upper = np.array([255, 100, 100])
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image, image, mask=mask)
show_image("Wyciągnięty czerwony kolor", result)