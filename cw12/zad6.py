import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
image = cv2.imread(cv2.samples.findFile("images/opencv.png"))
if image is None:
    print("Nie znaleziono loga")
B, G, R = cv2.split(image)
swapped = cv2.merge([R, G, B])
show_image("Zamieniono czerwony z niebieskim", swapped)

no_blue = image.copy()
no_blue[:, :, 0] = 0
show_image("Usunięto kanał niebieski", no_blue)