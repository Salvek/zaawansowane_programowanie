import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])
green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
result = cv2.bitwise_and(image, image, mask=green_mask)

show_image("Zielone obiekty", result)