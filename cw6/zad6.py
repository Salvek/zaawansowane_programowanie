import cv2
import imutils

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
h, w = image.shape[:2]

cv2.imshow("MYSZU", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
r = 400.0 / h
dim = (int(w * r), 400)
resized = imutils.resize(image, dim[0], dim[1])
cv2.imshow("Resized MYSZU", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
