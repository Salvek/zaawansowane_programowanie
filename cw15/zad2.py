import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_image)
s = cv2.add(s, 30)
modified_hsv = cv2.merge([h, s, v])
modified_image = cv2.cvtColor(modified_hsv, cv2.COLOR_HSV2BGR)

show_image("Originał", image)
show_image("Zmodyfikowany", modified_image)
