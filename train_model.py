from ultralytics import YOLO

# Load YOLOv8 pre-trained model
model = YOLO("yolov8n.pt")

# Train the model using the YAML data file
model.train(data="C:\\Users\\ag133\\Desktop\\coin_detection\\dataset\\dataset.yaml", epochs=50, imgsz=640)
