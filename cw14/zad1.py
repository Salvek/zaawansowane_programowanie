import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
blur_image = cv2.blur(image, (5, 5))
gaussian_blur_image = cv2.GaussianBlur(image, (5, 5), 0)
median_blur_image = cv2.medianBlur(image, 5)
bilateral_filter_image = cv2.bilateralFilter(image, 9, 75, 75)

show_image("Proste rozmycie", blur_image)
show_image("Rozmycie Gaussa", gaussian_blur_image)
show_image("Rozmycie medianowe", median_blur_image)
show_image("Rozmycie dwustronne", bilateral_filter_image)
