from flask import Flask, request, jsonify
from task_queue import add_task, get_task_status
from utils import count_people, download_image
import os

app = Flask(__name__)

# Foldery na zdjęcia
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# W kolejce przechowujemy zadania (prosty mechanizm w pamięci)
task_id_counter = 1

@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to the People Detection API!",
        "endpoints": {
            "POST /detect": "Upload a file to detect people.",
            "GET /detect-url": "Provide an image URL to detect people.",
            "GET /task/<task_id>": "Check the status of a task.",
        }
    })


@app.route('/detect', methods=['POST'])
def detect_local_file():
    global task_id_counter

    # Pobranie pliku z żądania POST
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Zapis pliku w folderze uploads
    img_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(img_path)

    # Dodanie zadania do kolejki
    task_id = f"task-{task_id_counter}"
    add_task(task_id, count_people, args=(img_path,))
    task_id_counter += 1

    return jsonify({"task_id": task_id}), 202


@app.route('/detect-url', methods=['GET'])
def detect_url():
    global task_id_counter

    # Pobranie URL zdjęcia
    img_url = request.args.get('url')
    if not img_url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        # Pobranie obrazu z URL do lokalnego folderu
        img_path = download_image(img_url, UPLOAD_FOLDER)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    # Dodanie zadania do kolejki
    task_id = f"task-{task_id_counter}"
    add_task(task_id, count_people, args=(img_path,))
    task_id_counter += 1

    return jsonify({"task_id": task_id}), 202


@app.route('/task/<task_id>', methods=['GET'])
def task_status(task_id):
    """Sprawdzanie statusu zadania."""
    result = get_task_status(task_id)
    if result is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)