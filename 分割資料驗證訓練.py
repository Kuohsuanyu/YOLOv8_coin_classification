import os
import random
import shutil

# Set paths for the dataset
base_dir = "C:\\Users\\ag133\\coin_detection\\dataset"
images_dir = os.path.join(base_dir, "images")
labels_dir = os.path.join(base_dir, "labels")

# Create directories for training and validation sets
train_images_dir = os.path.join(images_dir, "train")
val_images_dir = os.path.join(images_dir, "val")
train_labels_dir = os.path.join(labels_dir, "train")
val_labels_dir = os.path.join(labels_dir, "val")

os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# Get list of all image files
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Shuffle and split into 80% train and 20% validation
random.shuffle(image_files)
train_size = int(0.8 * len(image_files))
train_files = image_files[:train_size]
val_files = image_files[train_size:]

# Function to move files to their corresponding directories
def move_files(file_list, src_images_dir, src_labels_dir, dest_images_dir, dest_labels_dir):
    for image_file in file_list:
        image_path = os.path.join(src_images_dir, image_file)
        label_path = os.path.join(src_labels_dir, image_file.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg', '.txt'))
        
        if os.path.exists(label_path):  # Ensure corresponding label file exists
            shutil.move(image_path, dest_images_dir)
            shutil.move(label_path, dest_labels_dir)

# Move the training and validation files
move_files(train_files, images_dir, labels_dir, train_images_dir, train_labels_dir)
move_files(val_files, images_dir, labels_dir, val_images_dir, val_labels_dir)

print("Dataset split complete: 80% training and 20% validation.")
