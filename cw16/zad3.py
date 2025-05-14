import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

_, threshold_original = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
_, threshold_blurred = cv2.threshold(blurred_image, 100, 255, cv2.THRESH_BINARY)

show_image("Progowanie oryginalne", threshold_original)
show_image("Progowanie z rozmyciem", threshold_blurred)

