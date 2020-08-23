#!/usr/bin/python3
# _*_ coding: UTF-8 _*_


print ("helle python !")


import cv2
import os
 
output_dir ='/mnt/f/xlpython/'
i = 1
cap = cv2.VideoCapture(0)   # 打开笔记本的内置摄像头  参数是视频文件路径则打开视频
while 1:
    ret, frame = cap.read()  # 按帧读取图片  返回值ret代表是否读取 成功    frame 代表这一帧图像
    cv2.imshow('cap', frame)
    flag = cv2.waitKey(1)
    if flag == 13: # 按下回车键
        output_path = os.path.join(output_dir,  "%04d.jpg" % i)
        cv2.imwrite(output_path, frame)
        i += 1
    if flag == 27:  # 按下ESC键
        break
























