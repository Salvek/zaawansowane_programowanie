import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
h, w, _ = image.shape
mask = np.zeros((h, w), dtype=np.uint8)
mask[h // 3:2 * h // 3, w // 3:2 * w // 3] = 255

background_blurred = cv2.GaussianBlur(image, (15, 15), 0)
mask_colored = cv2.merge([mask, mask, mask])

final_image = np.where(mask_colored == 255, image, background_blurred)
show_image("Symulacja głębi ostrości", final_image)