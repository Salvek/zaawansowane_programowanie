import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_red = np.array([0, 100, 50])
upper_red = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)
lower_red2 = np.array([150, 100, 50])
upper_red2 = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = mask1 + mask2

red_channel = image[:, :, 2]
red_boost = cv2.add(red_channel, (mask > 0).astype(np.uint8) * 50)
image[:, :, 2] = np.clip(red_boost, 0, 255)
show_image("Wzmocnienie czerwonego przez maskę", image)