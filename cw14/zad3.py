import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
bilateral_image = cv2.bilateralFilter(image, 9, 75, 75)
show_image("Rozmycie dwustronne", bilateral_image)