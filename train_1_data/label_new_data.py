from ultralytics import YOLO


model = YOLO("C:\\Users\\ag133\\Desktop\\coin_detection\\runs\\detect\\train5\\weights\\best.pt")


model.predict(
    source="C:\\Users\\ag133\\Desktop\\coin_detection\\firsttrain_test\\all_coins",  
    save=True,                    
    save_txt=True,                
    imgsz=640,                    
    conf=0.5,                     
    project="C:\\Users\\ag133\\Desktop\\coin_detection\\firsttrain_test",  
    name="results",               
    exist_ok=True                
)
