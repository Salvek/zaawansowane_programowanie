import cv2

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
h = image.shape[0]

resized = cv2.resize(image, (800, h), interpolation=cv2.INTER_AREA)
cv2.imwrite("C:/Users/Salve/OneDrive/Obrazy/MYSZU_wide.jpeg", resized)