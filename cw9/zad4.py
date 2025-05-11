import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
modified = image.copy()
modified[:, :, 2] = np.clip(modified[:, :, 2] + 30, 0, 255)  # Red channel
modified[:, :, 1] = np.clip(modified[:, :, 1] - 20, 0, 255)  # Green channel
modified[:, :, 0] = np.clip(modified[:, :, 0] + 10, 0, 255)  # Blue channel
show_image("Filtr z Insta", modified)