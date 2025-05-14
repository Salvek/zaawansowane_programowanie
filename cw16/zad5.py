import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
brightened_image = cv2.add(gray_image, 50)
_, otsu_threshold = cv2.threshold(brightened_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

show_image("Progowanie Otsu", otsu_threshold)