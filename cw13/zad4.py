import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
closed_rect = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel_rect)
closed_ellipse = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel_ellipse)
show_image("Originał", image)
show_image("Zamknięcie kwadrat", closed_rect)
show_image("Zamknięcie elipsa", closed_ellipse)