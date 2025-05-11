import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
w = image.shape[1]
roi = image[:, w//2:]
show_image("Prawa połówka", roi)