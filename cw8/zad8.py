import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
h, w = image.shape[:2]
step = 10
for x in range(0, w-100, step):
    roi = image[:, x:x+100]
    show_image("Przesunięcie ROI", roi)
    cv2.waitKey(500)