# -*- coding: utf8 -*-
import cv2
if __name__=="__main__":
    cap=cv2.VideoCapture(1)
    timeF=25
    c=1
    num=1
    if cap.isOpened():
        while 1:
            ret,frame=cap.read()
            cv2.imshow("picture",frame)
            if(c%timeF==0):
                cv2.imwrite("./picture/Train3/"+str(num)+".jpg",frame)
                num=num+1
            c=c+1

            if cv2.waitKey(10)==0:
                break
    cv2.destroyAllWindows()