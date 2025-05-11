import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
numpy_result = np.clip(image - 80, 0, 255).astype(np.uint8)
opencv_result = cv2.subtract(image, np.full(image.shape, 80, dtype=np.uint8))
show_image("Przyciemnione przez NumPy", numpy_result)
show_image("Przyciemnione przez OpenCV", opencv_result)