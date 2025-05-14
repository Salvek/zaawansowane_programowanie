import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_skin = np.array([0, 20, 70])
upper_skin = np.array([20, 255, 255])
skin_mask = cv2.inRange(hsv_image, lower_skin, upper_skin)
result = cv2.bitwise_and(image, image, mask=skin_mask)

show_image("Wykrywanie skóry", result)