import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
B, G, R = cv2.split(image)
show_image("Blue Channel", B)
show_image("Green Channel", G)
show_image("Red Channel", R)
print("Które cechy pojawiają się silnie w jednym kanale i słabo w innych.")