import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def read_text(path):
    image = cv2.imread(path)

    if image is None:
        raise FileNotFoundError(f"Nie udało się wczytać obrazu: {path}")
    
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    methods = {
        "median_blur": cv2.medianBlur(image_grey, 3),
        "gaussian_blur_threshold": cv2.threshold(cv2.GaussianBlur(image_grey, (5, 5), 0), 0, 255,
                                                 cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        "bilateral_filter_threshold": cv2.threshold(cv2.bilateralFilter(image_grey, 5, 75, 75), 0, 255,
                                                     cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        "median_blur_threshold": cv2.threshold(cv2.medianBlur(image_grey, 3), 0, 255,
                                               cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        "adaptive_gaussian": cv2.adaptiveThreshold(cv2.GaussianBlur(image_grey, (5, 5), 0), 255,
                                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2),
        "adaptive_bilateral": cv2.adaptiveThreshold(cv2.bilateralFilter(image_grey, 9, 75, 75), 255,
                                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2),
        "adaptive_median": cv2.adaptiveThreshold(cv2.medianBlur(image_grey, 3), 255,
                                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2),
    }

    text = {}
    for method_name, processed_img in methods.items():
        txt = pytesseract.image_to_string(processed_img)
        text[method_name] = txt

    return text
    