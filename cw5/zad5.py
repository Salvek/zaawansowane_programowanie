import imutils
import cv2

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")

rotated = imutils.rotate(image, 180)
cv2.imshow("MYSZU Rotated by 180 Degrees", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()