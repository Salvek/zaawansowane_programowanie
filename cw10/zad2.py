import cv2
import numpy as np
from utils import show_image

image1 = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
image2 = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
h, w = image1.shape[:2]
image2 = cv2.resize(image2, (w, h))
if image1.shape != image2.shape:
    print("Obrazy muszą być tego samego rozmiaru")
diff = cv2.bitwise_xor(image1, image2)
show_image("Różnica XOR", diff)