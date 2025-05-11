import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
h, w = image.shape[:2]
grid_h, grid_w = h // 3, w // 3
for i in range(3):
    for j in range(3):
        roi = image[i*grid_h:(i+1)*grid_h, j*grid_w:(j+1)*grid_w]
        show_image(f"Grid {i},{j}", roi)