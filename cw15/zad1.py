import cv2
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
show_image("RGB", rgb_image)

r, g, b = cv2.split(rgb_image)
show_image("Kanał czerwony", r)
show_image("Kanał zielony", g)
show_image("Kanał niebieski", b)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
show_image("HSV", hsv_image)

h, s, v = cv2.split(hsv_image)
show_image("Barwy", h)
show_image("Nasycenie", s)
show_image("Wartość", v)
