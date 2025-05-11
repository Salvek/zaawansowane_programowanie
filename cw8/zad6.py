import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
roi = image[50:150, 50:150].copy()
target_h, target_w = roi.shape[:2]
h, w = image.shape[:2]
if 200 + target_h <= h and 200 + target_w <= w:
    image[200:200+target_h, 200:200+target_w] = roi
    show_image("Skopiowane ROI", image)
else:
    print("ROI wychodzi poza granice obrazu")