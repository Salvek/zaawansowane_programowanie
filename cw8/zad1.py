import cv2

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
roi = image[0:101, 0:101]
cv2.imshow("MYSZU ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()