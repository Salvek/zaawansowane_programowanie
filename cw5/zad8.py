import cv2

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)
for i in range(3):
    image = cv2.warpAffine(image, M, (w, h))
cv2.imshow("MYSZU Rotated by 3x30 Degrees", image)
cv2.waitKey(0)
cv2.destroyAllWindows()