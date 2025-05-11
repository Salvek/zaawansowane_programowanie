import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
startX = int(input("Wprowadź startowe X: "))
endX = int(input("Wprowadź końcowe X: "))
startY = int(input("Wprowadź startowe Y: "))
endY = int(input("Wprowadź końcowe Y: "))
roi = image[startY:endY, startX:endX]
show_image("Wybrane ROI", roi)