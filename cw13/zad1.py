import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
eroded_square = cv2.erode(image, kernel_square, iterations=1)
eroded_ellipse = cv2.erode(image, kernel_ellipse, iterations=1)
show_image("Originał", image)
show_image("Erozja kwadrat", eroded_square)
show_image("Erozja elipsa", eroded_ellipse)