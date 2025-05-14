import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# T = 30
_, threshold_30 = cv2.threshold(gray_image, 30, 255, cv2.THRESH_BINARY)
show_image("Progowanie T=30", threshold_30)

# T = 100
_, threshold_100 = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
show_image("Progowanie T=100", threshold_100)

# T = 200
_, threshold_200 = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
show_image("Progowanie T=200", threshold_200)













