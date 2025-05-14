import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
kernel_sizes = [(3, 3), (5, 5), (9, 9), (15, 15)]

for kernel_size in kernel_sizes:
    blur_image = cv2.blur(image, kernel_size)
    show_image(f"wpływ rozmiaru kernela na efekt rozmycia {kernel_size}", blur_image)