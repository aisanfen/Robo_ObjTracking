import numpy as np
import cv2
from function import func_add
from naturenet.mynet import  Node

from naturenet.motion_detection import compare_by_RGB
if __name__ == '__main__':

    #相似度阈值
    threshold_value=1
    cap = cv2.VideoCapture (1)

    node1=Node(0,0)
    path="D:/code/opencv_lab/classifier_data/haarcascade_frontalface_alt.xml"
    while True:
        if cap.isOpened ():
            flag=False
            count=0
            ret, frame = cap.read ()
            # 调用OpenCV原生级联分类器API
            face = cv2.CascadeClassifier (path)
            # 转换图像为灰度图
            gray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)
            # 人脸位置标定，最大滑动窗口像素5，最小1.3
            faces = face.detectMultiScale (gray, 1.3, 5)
            img = np.zeros ((len(frame), len(frame[0]), 3), np.uint8)
            # 遍历搜索到的人脸图像，返回点集的人脸右上角坐标(x,y)
            # 人脸区域宽度w高度h
            # PS:每一帧图像中的人脸个数是len(faces) faces是个数组
            if len(faces)>0:
                for x, y, w, h in faces:
                # 画正方形(x,y)为正方形左上角起始点
                # x+w为宽度结束点 y+h为高度结束点
                # (0,0,255)正方形边缘为红色
                # 2边界线像素为2
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                #比较当前帧,记录中心点
                    new_node=Node(x+w/2,y+h/2)
                    node1.add (new_node)
                    break
            if node1.getLength()>2:
                p = node1.pnext
                while p.pnext != None:
                    try:
                        cv2.line(img, (int(p.x), int(p.y)), (int(p.pnext.x), int(p.pnext.y)), (0, 0, 255), 5)
                    except Exception as e:
                        print(e)
                        pass
                    finally:
                        p = p.pnext
            # if node1.getLength() >= 5:
            #     node1=node1.pnext
            cv2.imshow ("image", frame)
            # 画线
            p=node1
            cv2.imshow ("drawline", img)
            if cv2.waitKey (10) == 'q':
                break
    cv2.destroyAllWindows ()
