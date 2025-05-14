import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
brightened_image = cv2.add(gray_image, 50)

_, threshold_original = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
_, threshold_brightened = cv2.threshold(brightened_image, 100, 255, cv2.THRESH_BINARY)

show_image("Progowanie oryginalne", threshold_original)
show_image("Progowanie rozjaśnione", threshold_brightened)