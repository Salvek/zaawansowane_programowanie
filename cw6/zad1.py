import cv2

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
h, w = image.shape[:2]

cv2.imshow("MYSZU", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
resized = cv2.resize(image, (w // 2, h // 2), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized MYSZU", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
