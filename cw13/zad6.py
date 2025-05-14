import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
# Zwiększenie czytelności tablic rejestracyjnych
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
show_image("Originał", image)
show_image("Bezprogowy", thresh)
show_image("Po zamknięciu morfologicznym", closed)