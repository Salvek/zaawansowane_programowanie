import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
red_mask = cv2.inRange(hsv_image, lower_red, upper_red)

lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])
blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])
green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

combined_mask = cv2.bitwise_or(red_mask, cv2.bitwise_or(blue_mask, green_mask))

result = cv2.bitwise_and(image, image, mask=combined_mask)

show_image("Segmentcaja kolorów", result)