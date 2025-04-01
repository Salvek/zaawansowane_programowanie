import cv2

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
h, w = image.shape[:2]

p = 1.0
while p <= 3.0:
    image = cv2.resize(image, (int(w * p), int(h * p)), interpolation=cv2.INTER_AREA)
    cv2.imshow(f"Resized MYSZU by {int(p*100)}%", image)
    cv2.waitKey(500)
    p = round(p + 0.2, 1)