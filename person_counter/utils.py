import cv2
import numpy as np
import requests
import os

def count_people(image_path):
    """Licz osoby na obrazie."""
    img = cv2.imread(image_path)
    # Detekcja ludzi (symulowana, nie ma modelu TensorFlow)
    h, w, _ = img.shape
    return np.random.randint(1, 10)  # Przykładowa liczba


def download_image(url, save_folder):
    """Pobierz obraz z URL."""
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise Exception("Unable to download image")
    filename = os.path.join(save_folder, os.path.basename(url))
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    return filename
