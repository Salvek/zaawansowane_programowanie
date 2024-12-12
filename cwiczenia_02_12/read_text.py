import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def read_text(path):
    image = cv2.imread(path)

    if image is None:
        raise FileNotFoundError(f"Nie udało się wczytać obrazu: {path}")
    
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    processed_image = cv2.adaptiveThreshold(image_grey, 255,
                                          cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY, 11, 2)
    
    text = pytesseract.image_to_string(processed_image, lang='eng')

    return text
    