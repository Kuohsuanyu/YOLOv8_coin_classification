import os
import time

# Define paths for the labels and images folders
label_folder = "C:\\Users\\ag133\\coin_detection\\images\\labelled\\labels"
image_folder = "C:\\Users\\ag133\\coin_detection\\images\\labelled\\images"

# Function to safely remove a file with retries
def safe_remove(file_path):
    for attempt in range(3):  # Try up to 3 times
        try:
            os.remove(file_path)
            print(f"Successfully removed: {file_path}")
            return
        except PermissionError:
            print(f"Permission error encountered. Retrying {file_path}...")
            time.sleep(0.5)  # Wait a short time before retrying
    print(f"Failed to remove {file_path} after several attempts.")

# Loop through label files and remove files without labels and their corresponding images
for label_file in os.listdir(label_folder):
    label_path = os.path.join(label_folder, label_file)
    image_path = os.path.join(image_folder, label_file.replace(".txt", ".jpg"))  # Assuming images are in JPG format

    # Check if label file is empty; if so, delete the label file and corresponding image
    if os.path.isfile(label_path):
        with open(label_path, "r") as file:
            if os.stat(label_path).st_size == 0:
                safe_remove(label_path)
                if os.path.exists(image_path):
                    safe_remove(image_path)

# Loop through label files again to remove files with multiple labels and their corresponding images
for label_file in os.listdir(label_folder):
    label_path = os.path.join(label_folder, label_file)
    image_path = os.path.join(image_folder, label_file.replace(".txt", ".jpg"))

    # Check if the label file has multiple labels; if so, delete the label file and corresponding image
    with open(label_path, "r") as file:
        lines = file.readlines()
        if len(lines) > 1:  # If there are multiple lines in the label file
            safe_remove(label_path)
            if os.path.exists(image_path):
                safe_remove(image_path)

print("Cleanup complete: retained only images with a single 'coin' label.")
