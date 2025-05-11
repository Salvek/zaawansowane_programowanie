import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
h, w = image.shape[:2]
mask = np.zeros((h, w), dtype="uint8")
center = (w // 2, h // 2)
axes = (w // 4, h // 3)
cv2.ellipse(mask, center, axes, 0, 0, 360, 1, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
show_image("Maskowanie obszaru twarzy", masked)