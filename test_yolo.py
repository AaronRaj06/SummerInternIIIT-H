# from ultralytics import YOLO

# print("Loading model...")
# model = YOLO("yolov8n-seg.pt")

# print("Running prediction...")
# results = model.predict("https://ultralytics.com/images/bus.jpg", save=True)

# print("Prediction complete.")
# print("Check the 'runs/segment' folder for output image.")


from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")

# Replace the URL or local file path below
results = model.predict(
    source=r"C:\Users\Aaron\Desktop\IIIT-H\Summer Internship\Task-1\RusselWestBrook.jpg",
    save=True
)

print("Segmentation done. Check the 'runs/segment' folder.")
