import cv2
import math
def compare_by_RGB(image_1,image_2):
    """
    :param image_1:
    :param image_2:
    :return:
    """
    G_1 = 0
    B_1 = 0
    R_1 = 0
    G_2 = 0
    B_2 = 0
    R_2 = 0
    #第一个图像的通道和
    for x in image_1:
        for y in x:
            G_1 +=y[0]
            B_1 += y[1]
            R_1 += y[2]
    #第二个图像通道和
    for x in image_1:
        for y in x:
            G_2 +=y[0]
            B_2 += y[1]
            R_2 += y[2]
    #图像矩阵在各通道相似度
    inc_G = 1 - math.fabs(G_1 - G_2) / G_2
    inc_B = 1 - math.fabs(B_1 - B_2) / B_2
    inc_R = 1 - math.fabs(R_1 - R_2) / R_2