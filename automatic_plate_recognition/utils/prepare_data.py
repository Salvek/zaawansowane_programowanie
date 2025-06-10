import os
import random
import shutil
import xml.etree.ElementTree as ET

output_dir = os.path.join(os.path.dirname(__file__), '..', 'dataset')
photos_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'photos')
xml_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'annotations.xml')

train_images_dir = os.path.join(output_dir, 'images/train')
test_images_dir = os.path.join(output_dir, 'images/test')

train_labels_dir = os.path.join(output_dir, 'labels/train')
test_labels_dir = os.path.join(output_dir, 'labels/test')

os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(test_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(test_labels_dir, exist_ok=True)

def save_yolo_labels(image_element, label_file_path):
    """
    Zapisuje plik YOLO z bounding boxami dla pojedynczego obrazu.
    """
    width = float(image_element.get('width'))
    height = float(image_element.get('height'))

    yolo_lines = []
    for box in image_element.findall('box'):
        if box.get('label') != 'plate':
            continue

        xtl = float(box.get('xtl'))
        ytl = float(box.get('ytl'))
        xbr = float(box.get('xbr'))
        ybr = float(box.get('ybr'))

        # konwersja do formatu YOLO (x_center, y_center, width, height)
        x_center = ((xtl + xbr) / 2) / width
        y_center = ((ytl + ybr) / 2) / height
        box_width = (xbr - xtl) / width
        box_height = (ybr - ytl) / height

        class_id = 0  # zakładamy, że plate ma id 0
        yolo_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}")

    with open(label_file_path, 'w') as f:
        f.write('\n'.join(yolo_lines))

# Wczytanie XML
tree = ET.parse(xml_path)
root = tree.getroot()
annotations = [img.get('name') for img in root.findall('image')]

# Podział zdjęć
all_photos = [p for p in os.listdir(photos_dir) if p.endswith(('.png', '.jpg'))]
random.shuffle(all_photos)

split_index = int(0.7 * len(all_photos))
train_files = all_photos[:split_index]
test_files = all_photos[split_index:]


train_labels = []
test_labels = []

# Przetwarzamy obrazy i zbieramy etykiety
for image in root.findall('image'):
    filename = image.get('name')
    src_path = os.path.join(photos_dir, filename)

    plate_numbers = []
    for box in image.findall('box'):
        if box.get('label') == 'plate':
            attr = box.find("attribute[@name='plate number']")
            if attr is not None:
                plate_numbers.append(attr.text.strip())

    label_str = ','.join(plate_numbers) if plate_numbers else 'no_plate'

    if filename in train_files:
        dst_path = os.path.join(train_images_dir, filename)
        train_labels.append(f"{dst_path} {label_str}")
        label_file_path = os.path.join(train_labels_dir, os.path.splitext(filename)[0] + '.txt')
    elif filename in test_files:
        dst_path = os.path.join(test_images_dir, filename)
        test_labels.append(f"{dst_path} {label_str}")
        label_file_path = os.path.join(test_labels_dir, os.path.splitext(filename)[0] + '.txt')
    else:
        # Pomijamy pliki, których nie ma w train/test
        continue

    # Kopiujemy obraz
    shutil.copyfile(src_path, dst_path)

    # Zapisujemy plik z bounding boxami YOLO
    save_yolo_labels(image, label_file_path)


print(f"{len(train_files)} plików do train i {len(test_files)} do test")