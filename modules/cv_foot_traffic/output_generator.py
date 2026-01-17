import os
import pandas as pd
from model import count_people

BASE_DIR = r"data\raw\cv_foot_traffic"
OUT_PATH = r"data\outputs\cv_foot_traffic.csv"

rows = []

for zone_folder in sorted(os.listdir(BASE_DIR)):
    zone_path = os.path.join(BASE_DIR, zone_folder)

    if not os.path.isdir(zone_path):
        continue

    images_dir = os.path.join(zone_path, "images")
    if not os.path.exists(images_dir):
        continue

    zone_id = zone_folder 

    for img_name in sorted(os.listdir(images_dir)):
        if not img_name.lower().endswith(".png"):
            continue

        img_path = os.path.join(images_dir, img_name)
        people_count = count_people(img_path)

        rows.append({
            "timestamp": img_name,   # placeholder till real cctv 
            "zone_id": zone_id,
            "people_count": people_count
        })

df = pd.DataFrame(rows)
os.makedirs("../../data/outputs", exist_ok=True)
df.to_csv(OUT_PATH, index=False)

print("Saved:", OUT_PATH)
print(df.head())
