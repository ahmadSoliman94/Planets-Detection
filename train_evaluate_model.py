
from  ultralytics import YOLO

def train_model(model,config_path,epochs,image_size,val=True):
    
    # train model
    model.train(
        data = config_path,
        epochs = epochs,
    	val=val,
        imgsz=image_size)
    
    # evaluate the model on the val-set
    results = model.val()
    print(results)
