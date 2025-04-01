import cv2
import numpy as np

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")

cv2.imshow("MYSZU", image)
flipped_half = cv2.flip(image[0 : len(image), len(image[0]) // 2 :], 0)
left_half = image[: len(image), : len(image[0]) // 2]
flipped = np.concatenate((left_half, flipped_half), axis=1)
cv2.imshow("MYSZU Halfly Flipped", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()