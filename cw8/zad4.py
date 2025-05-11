import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
startX = int(input("Enter startX: "))
endX = int(input("Enter endX: "))
startY = int(input("Enter startY: "))
endY = int(input("Enter endY: "))
roi = image[startY:endY, startX:endX]
show_image("User Selected ROI", roi)