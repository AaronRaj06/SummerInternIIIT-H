from ultralytics import YOLO
import os

model = YOLO("yolov8n-seg.pt")

input_dir = "frames"
output_dir = "segmented_frames"
os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):
    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_dir, file)
        output_path = os.path.join(output_dir, file)
        results = model(input_path)
        results[0].save(filename=output_path)
        print(f"Segmented: {file}")

