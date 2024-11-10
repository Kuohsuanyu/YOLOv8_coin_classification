# -*- coding: utf-8 -*-
import os
from ultralytics import YOLO

# Initialize YOLOv8 model (Nano model)
model = YOLO("yolov8n.pt")  # Using locally downloaded yolov8n.pt

# Define source folder and output folder for images and labels
source_folder = "C:\\Users\\ag133\\coin_detection\\images\\unlabelled"
output_folder = "C:\\Users\\ag133\\coin_detection\\images\\labelled"

# Perform YOLO detection and save results as YOLO format labels
results = model.predict(source=source_folder, save=True, save_txt=True, project=output_folder, name="labelled", imgsz=640, device="cpu")

# Iterate through generated label files and modify class to "coin"
label_folder = os.path.join(output_folder, "labelled", "labels")
for filename in os.listdir(label_folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(label_folder, filename)
        with open(filepath, "r") as file:
            lines = file.readlines()
        
        # Set all labels to "coin" (e.g., set class index to 0)
        new_lines = ["0 " + " ".join(line.split()[1:]) + "\n" for line in lines]
        
        # Write modified content back to file
        with open(filepath, "w") as file:
            file.writelines(new_lines)

print("All labels changed to 'coin'")
