import cv2
import numpy as np
import os
path='D:\code\Target_tracking\picture\Train3'
def listdir(path,list_name):
    for file in os.listdir(path):
        file_path=os.path.join(path,file)
        if os.path.isdir(file_path):
            listdir(file_path,list_name)
        else:
            list_name.append({"path":file_path,"name":file,"dir":path})

#对图像进行缩放
def picture_zoom(image):
    num=1
    image_enlarge=cv2.resize(image,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
    cv2.imwrite (".\picture\text" + str (num) + ".jpg", frame)