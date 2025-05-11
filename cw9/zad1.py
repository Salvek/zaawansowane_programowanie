import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
numpy_result = np.clip(image + 50, 0, 255).astype(np.uint8)
opencv_result = cv2.add(image, np.full(image.shape, 50, dtype=np.uint8))
show_image("Zwiększona jasność przez NumPy", numpy_result)
show_image("Zwiększona jasność przez OpenCV", opencv_result)