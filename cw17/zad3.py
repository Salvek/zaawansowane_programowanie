import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold_mean = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
show_image("Progowanie Adaptacyjne C", threshold_mean)

threshold_gaussian = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
show_image("Progowanie Adaptacyjne Gaussa C", threshold_gaussian)

c_values = [2, 5, 10, 15]
for c in c_values:
    threshold_mean_c = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, c)
    show_image(f"Mean C={c}", threshold_mean_c)

    threshold_gaussian_c = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, c)
    show_image(f"Gaussa C={c}", threshold_gaussian_c)