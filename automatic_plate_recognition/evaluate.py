import xml.etree.ElementTree as ET
from pathlib import Path
from ultralytics import YOLO
import cv2
import re
import time
import Levenshtein
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

model_path = Path("C:/Users/Salve/workspaces/zaawansowane_programowanie/runs/plate/weights/best.pt")
test_dir = Path("./dataset/images/test/")
annotation_path = Path("./data/annotations.xml")
cropped_dir = Path("cropped")

cropped_dir.mkdir(exist_ok=True)
for f in cropped_dir.glob("*"): f.unlink()

# === FUNKCJE ===

def parse_annotations(xml_path):
    tree = ET.parse(xml_path)
    return {
        image.attrib["name"]: image.find('box/attribute[@name="plate number"]').text.strip().upper()
        for image in tree.getroot().findall("image")
        if image.find('box/attribute[@name="plate number"]') is not None
    }

def enhance_plate_image(image):
    height, width = image.shape[:2]
    cut_pixels_left = max(1, int(width * 0.1))  
    cut_pixels_right = max(1, int(width * 0.02)) 
    cut_pixels_top = max(1, int(height * 0.048))
    cut_pixels_bottom = max(1, int(height * 0.045))

    image = image[cut_pixels_top : height - cut_pixels_bottom, cut_pixels_left : width - cut_pixels_right]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    filtered = cv2.bilateralFilter(gray, d=11, sigmaColor=90, sigmaSpace=90)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(filtered)

    thresh = cv2.adaptiveThreshold(
        enhanced,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        301, 25
    )

    inverted = cv2.bitwise_not(thresh)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    opened = cv2.morphologyEx(inverted, cv2.MORPH_OPEN, kernel, iterations=1)

    dilated = cv2.dilate(opened, kernel, iterations=1)

    closed = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel, iterations=1)

    thick_text = cv2.bitwise_not(closed)

    return thick_text

    
def ocr_and_clean(image):
    config = r'--psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT, config=config, lang='pol')
    text = ''.join([data['text'][i].strip() for i in range(len(data['text']))
                    if data['conf'][i] != '-1' and re.fullmatch(r'[A-Z0-9]+', data['text'][i].strip())])
    text = re.sub(r'[^A-Z0-9]', '', text.upper())

    if not text:
        return ""

    # Korekta pierwszego znaku, jeśli to cyfra, zamieniamy na literę
    corrections = {'0': 'O', '1': 'I', '5': 'S', '4': 'A', '6': 'S', '7': 'Z', '2': 'Z', '3': 'S', '8': 'B', '9': 'S'}
    if text[0].isdigit():
        text = corrections.get(text[0], text[0]) + text[1:]

    # Pierwszy znak musi być teraz literą
    if not text[0].isalpha():
        return ""

    return text if 3 <= len(text) <= 8 else ""

def calculate_final_grade(accuracy_percent, processing_time_sec):
    if accuracy_percent < 60 or processing_time_sec > 60:
        return 2.0
    acc_norm = (accuracy_percent - 60) / 40
    time_norm = (60 - processing_time_sec) / 50
    score = 0.7 * acc_norm + 0.3 * time_norm
    return round((2.0 + 3.0 * score) * 2) / 2

# === GŁÓWNY KOD ===

plate_map = parse_annotations(annotation_path)
model = YOLO(model_path)
images = sorted(list(test_dir.glob("*.jpg")))

correct = 0
start = time.time()

for path in images:
    fname = path.name
    expected = plate_map.get(fname)
    if not expected:
        print(f"{fname}: brak adnotacji")
        continue

    img = cv2.imread(str(path))
    if img is None:
        print(f"{fname}: nie można wczytać")
        continue

    results = model.predict(source=str(path), conf=0.7, save=False, show=False, verbose=False)
    if not results[0].boxes:
        print(f"{fname}: brak detekcji")
        continue

    x1, y1, x2, y2 = map(int, results[0].boxes.xyxy[0].cpu().numpy())
    plate_img = img[y1:y2, x1:x2]

    enhanced = enhance_plate_image(plate_img)
    detected = ocr_and_clean(enhanced)

    cv2.imwrite(str(cropped_dir / f"{fname}_cropped.png"), enhanced)

    if not detected:
        print(f"{fname}: niepoprawny OCR")
        continue

    dist = Levenshtein.distance(detected, expected)
    if (expected in detected) or (dist <= 1):
        correct += 1
        print(f" {expected} -> {detected}")
    else:
        print(f" {detected} ≠ {expected}")


elapsed = time.time() - start
total = len(images)
accuracy = (correct / total) * 100
proc_time = (elapsed / total) * 100
grade = calculate_final_grade(accuracy, proc_time)

print("\nPODSUMOWANIE:")
print(f"Skuteczność: {accuracy:.2f}%")
print(f"Czas przetwarzania: {proc_time:.2f} s")
print(f"Ocena końcowa: {grade}")