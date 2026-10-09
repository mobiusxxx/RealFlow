'''
Author: xiafanli xiafanli@eccom.com.cn
Date: 2023-10-26 15:48:11
Description: 
'''
import sys
sys.path.append("../")
import cv2
import os


def save_img():
    video_path = 'F:/datasets/water_datasets/create_data/val/origin_videos/'
    img_path = './test_data/'
    # if not os.path.exists(img_path):
    #     os.makedirs(img_path)
    videos = os.listdir(video_path)
    for video_name in videos:
        file_name = video_name.split('.')[0]
        folder_name = img_path + file_name
        # if not os.path.exists(folder_name):
        #     os.makedirs(folder_name)
        print(video_path+video_name)
        vc = cv2.VideoCapture(video_path+video_name) #读入视频文件
        c = 0
        i = 0
        rval=vc.isOpened()

        while rval:   #循环读取视频帧
            c = c + 1
            rval, frame = vc.read()
            if frame is None:
                break
            #改变图片的分辨率
            frame = cv2.resize(frame, (640, 640), interpolation=cv2.INTER_CUBIC)
            pic_path = './test_data/val_image'+'/'
            if rval and c % 5 == 0:
                i = i+1
                cv2.imwrite(pic_path + file_name + '_' + str(i) + '.jpg', frame)
                print(pic_path + file_name + '_' + str(i) + '.jpg')
                cv2.waitKey(1)
            elif not rval:
                break
        vc.release()
        print('save_success')
        print(folder_name)

save_img()
