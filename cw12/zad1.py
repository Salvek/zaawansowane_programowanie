import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
B, G, R = cv2.split(image)
show_image("Kanał Niebieski", B)
show_image("Kanał Zielony", G)
show_image("Kanał Czerwony", R)
cv2.imwrite("blue_channel.jpg", B)
cv2.imwrite("green_channel.jpg", G)
cv2.imwrite("red_channel.jpg", R)