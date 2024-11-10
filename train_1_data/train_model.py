from ultralytics import YOLO

# 加載已訓練的模型（best.pt）
model = YOLO("C:/Users/ag133/Desktop/coin_detection/runs/detect/train5/weights/best.pt")

# 開始進一步訓練
model.train(
    data="C:/Users/ag133/Desktop/coin_detection/dataset2/dataset.yaml",  # 指向新數據集的 .yaml 文件
    epochs=100,             # 設置需要進行的 epoch 次數，可根據需求調整
    imgsz=640,              # 訓練圖片的大小
    batch=16,               # 訓練批次大小，可根據硬體資源調整
    save=True,              # 訓練後保存結果
    project="C:/Users/ag133/Desktop/coin_detection/run2",  # 指定總的保存路徑
    name="fine_tune_run"    # 指定訓練結果的名稱，避免覆蓋
)
