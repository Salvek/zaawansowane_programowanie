import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
noise_image = image.copy()
noise_image = np.uint8(np.random.normal(0, 25, noise_image.shape) + noise_image)
show_image("Zaszumiony obraz", noise_image)

blur_image = cv2.blur(noise_image, (5, 5))
gaussian_blur_image = cv2.GaussianBlur(noise_image, (5, 5), 0)
median_blur_image = cv2.medianBlur(noise_image, 5)
bilateral_filter_image = cv2.bilateralFilter(noise_image, 9, 75, 75)

show_image("Rozmycie proste", blur_image)
show_image("Rozmycie Gaussa", gaussian_blur_image)
show_image("Rozmycie medianowe", median_blur_image)
show_image("Rozmycie dwustronne", bilateral_filter_image)