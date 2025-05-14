import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hsv_image[:, :, 0] = hsv_image[:, :, 0] + 30
modified_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

show_image("Originał", image)
show_image("Zmodyfikowany", modified_image)