import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
roi = image[:300, :300]
cv2.imwrite("MYSZU_cropped.jpg", roi)
show_image("Zapisano przycięty obraz", roi)