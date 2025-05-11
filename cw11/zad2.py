import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
h, w = image.shape[:2]
mask = np.ones((h, w), dtype="uint8") * 255
eye_region = (w//2, h//2, w//2, h//10)
x, y, ew, eh = eye_region
cv2.rectangle(mask, (x - x // 2, y - y // 4), (x+ew, y+eh), 0, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
show_image("Zasłonięte oczy", masked)