import cv2
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/Salve/OneDrive/Obrazy/MYSZU.jpeg")
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
fig, axs = plt.subplots(1, 4, figsize=(15, 5))
axs[0].imshow(image, cmap='gray')
axs[0].set_title("Originał")
axs[0].axis('off')
for i in range(1, 4):
    dilated = cv2.dilate(image, kernel, iterations=i)
    axs[i].imshow(dilated, cmap='gray')
    axs[i].set_title(f"Dylatacja {i}")
    axs[i].axis('off')
plt.tight_layout()
plt.show()