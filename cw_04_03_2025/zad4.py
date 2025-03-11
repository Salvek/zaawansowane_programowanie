# 4. Zamiana wartości piksela na czarny
#     a. Pobierz od użytkownika współrzędne (x, y) .
#     b. Stwórz walidację, która zweryfikuje czy podane współrzędne nie
#     wychodzą poza wymiar zdjęcia.
#     c. Ustaw piksel w tym miejscu na czarny (0, 0, 0) .

import cv2
image = cv2.imread('image.jpeg')

h, w, _ = image.shape

while True:
    try:
        x, y = map(int, input('Please enter x, y: ').split())
        if 0 <= x < w and 0 <= y < h:
            image[y, x] = (0, 0, 0)
            cv2.imshow("Modified Image", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break
        else:
            print(f"Wrong coordinates. Please enter values within the image dimensions: {h} x {w}")
    except ValueError:
        print('Invalid input. Enter two integers separated by space.')

