import cv2
import numpy as np
from utils import show_image

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
shape = (300, 300)
triangle = np.zeros(shape, dtype=np.uint8)
circle = np.zeros(shape, dtype=np.uint8)

pts = np.array([[150, 50], [100, 250], [200, 250]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(triangle, [pts], 255)
cv2.circle(circle, (150, 150), 100, 255, -1)

and_result = cv2.bitwise_and(triangle, circle)
or_result = cv2.bitwise_or(triangle, circle)
xor_result = cv2.bitwise_xor(triangle, circle)
not_triangle = cv2.bitwise_not(triangle)

show_image("Trójkąt", triangle)
show_image("Okrąg", circle)
show_image("AND", and_result)
show_image("OR", or_result)
show_image("XOR", xor_result)
show_image("NOT", not_triangle)