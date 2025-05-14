import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
kernels = {
    "kwadrat": cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)),
    "krzyz": cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5)),
    "elipsa": cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
}
for name, kernel in kernels.items():
    eroded = cv2.erode(image, kernel)
    dilated = cv2.dilate(image, kernel)
    opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    show_image(f"{name} - Erozja", eroded)
    show_image(f"{name} - Dylatacja,", dilated)
    show_image(f"{name} - Otwarcie", opened)
    show_image(f"{name} - Zamknięcie", closed)
    show_image(f"{name} - Gradient", gradient)