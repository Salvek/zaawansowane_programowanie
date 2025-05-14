import cv2

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

_, otsu_threshold = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
otsu_value = _
