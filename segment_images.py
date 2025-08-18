# from ultralytics import YOLO
# import os

# # Load segmentation model
# model = YOLO('yolov8n-seg.pt')  # You can also use yolov8s-seg.pt for more accuracy

# # Input and output folders
# input_dir = 'images'
# output_dir = 'segmented_images'
# os.makedirs(output_dir, exist_ok=True)

# # Process each image in input folder
# for file in os.listdir(input_dir):
#     if file.lower().endswith(('.jpg', '.jpeg', '.png')):
#         image_path = os.path.join(input_dir, file)
#         results = model(image_path)

#         # Save segmented output image (with masks)
#         results[0].save(filename=os.path.join(output_dir, file))
from ultralytics import YOLO
import os

model = YOLO('yolov8n-seg.pt')

input_dir = 'images'
output_dir = 'segmented_images'
os.makedirs(output_dir, exist_ok=True)

# Get already segmented filenames
already_segmented = set(os.listdir(output_dir))

# Process only unsegmented images
for file in os.listdir(input_dir):
    if file.lower().endswith(('.jpg', '.jpeg', '.png')) and file not in already_segmented:
        image_path = os.path.join(input_dir, file)
        results = model(image_path)
        results[0].save(filename=os.path.join(output_dir, file))
        print(f"[✓] Newly segmented: {file}")

