import imutils
import cv2

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")

rotated = imutils.rotate(image, 75)
cv2.imwrite("C:/Users/Salve/OneDrive/Obrazy/MYSZU_output.jpeg", rotated)
cv2.imshow("MYSZU Rotated by 75 Degrees", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()