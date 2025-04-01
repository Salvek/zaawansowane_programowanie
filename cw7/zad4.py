import cv2

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")

cv2.imshow("MYSZU", image)
cv2.imshow("Original MYSZU", image)

flipped = cv2.flip(image, 1)
cv2.imshow("MYSZU Flipped Horizontally", flipped)

flipped = cv2.flip(image, 0)
cv2.imshow("MYSZU Flipped Vertically", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("MYSZU Flipped Horizontally & Vertically", flipped)


cv2.waitKey(0)
cv2.destroyAllWindows()