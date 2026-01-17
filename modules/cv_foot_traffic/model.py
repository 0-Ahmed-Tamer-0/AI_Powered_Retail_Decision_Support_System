from ultralytics import YOLO

model = YOLO(r"modules\cv_foot_traffic\runs\detect\train\weights\best.pt")

def count_people(image_path):
    results = model(image_path)
    return len(results[0].boxes)
