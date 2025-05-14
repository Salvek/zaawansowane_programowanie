import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_image)
s_low = cv2.subtract(s, 50)
s_high = cv2.add(s, 50)

show_image("Original Image", image)
show_image("Low Saturation Image", cv2.cvtColor(cv2.merge([h, s_low, v]), cv2.COLOR_HSV2BGR))
show_image("High Saturation Image", cv2.cvtColor(cv2.merge([h, s_high, v]), cv2.COLOR_HSV2BGR))
