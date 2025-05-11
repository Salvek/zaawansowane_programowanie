import cv2

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
roi = image[0 : len(image) // 2, 0:-1]
cv2.imshow("MYSZU Lower Half", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()