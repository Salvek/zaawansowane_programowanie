import cv2

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
cv2.imshow("MYSZU", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("MYSZU Rotated by -90 Degrees", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()