from ultralytics import YOLO
from pathlib import Path

def train_yolo():
    data_path = Path(__file__).parent / "utils" / "data.yaml"
    project_path = Path(__file__).parent.parent / "runs"

    model = YOLO("yolov8n.pt")

    model.train(
        data=str(data_path),
        epochs=25,
        imgsz=640,
        project=str(project_path),
        workers=4,
        cache=True,
        name="plate",
        exist_ok=True,
        save=True
    )

if __name__ == "__main__":
    train_yolo()