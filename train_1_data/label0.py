import os

# 資料集標籤資料夾路徑
label_folder = "C:\\Users\\ag133\\Desktop\\coin_detection\\ohcoindata\\valid\\labels"

# 遍歷標籤文件並統一類別為「硬幣」（假設索引為 0）
for label_file in os.listdir(label_folder):
    if label_file.endswith(".txt"):
        file_path = os.path.join(label_folder, label_file)
        with open(file_path, "r") as file:
            lines = file.readlines()

        # 修改類別索引為 0
        new_lines = ["0 " + " ".join(line.split()[1:]) + "\n" for line in lines]

        # 覆寫原標籤文件
        with open(file_path, "w") as file:
            file.writelines(new_lines)

print("All labels have been changed to a single class 'coin'.")
