import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
show_image("Origina", image)
show_image("Odszumione", opened)