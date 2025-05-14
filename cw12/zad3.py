import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
B, G, R = cv2.split(image)
merged_rgb = cv2.merge([R, B, G])
show_image("Zamienione kanały (R, B, G)", merged_rgb)