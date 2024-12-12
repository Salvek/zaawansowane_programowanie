import os
from read_text import read_text

image_path = os.path.join(os.path.dirname(__file__), r"images/TEST1.png")

print(read_text(image_path))