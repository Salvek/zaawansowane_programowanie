import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, threshold_simple = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
show_image("Progowanie Podstawowe", threshold_simple)

_, threshold_otsu = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
show_image("Progowanie Otsu", threshold_otsu)

threshold_mean = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
show_image("Progowanie Adaptacyjne", threshold_mean)

threshold_gaussian = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
show_image("Progowanie Adaptacyjne Gaussa", threshold_gaussian)















