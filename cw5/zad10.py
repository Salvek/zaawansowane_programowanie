import imutils
import cv2

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
angle = 0

while angle < 360:
    image = imutils.rotate(image, 15)
    cv2.imshow("MYSZU Rotated", image)
    cv2.waitKey(400)
    cv2.destroyAllWindows()
    angle += 15