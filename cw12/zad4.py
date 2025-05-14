import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
B, G, R = cv2.split(image)
R = cv2.add(R, 50)
merged = cv2.merge([B, G, R])
show_image("Wzmocniony kanał czerwony", merged)