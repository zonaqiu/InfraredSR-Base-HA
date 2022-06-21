# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:53:28 2020

@author: 陨星落云
"""
import os

import imageio
import numpy as np

# HR_path = './lr/'
SR_path = './output/save_results/'
save_path = './output/one_channel/'
total_num=0
if not os.path.isdir(save_path):
    os.makedirs(save_path)

for SR_filename in os.listdir(SR_path):
    SR = imageio.imread(SR_path+SR_filename)
    h,w,c = SR.shape
    one_channel = 0.2126*SR[:,:,0] + 0.7152*SR[:,:,1] + 0.0722*SR[:,:,2]
    # print(one_channel.shape)
    one_channel_img = one_channel.reshape(h,w).astype(np.uint8)
    imageio.imsave(save_path+SR_filename,one_channel_img)
    total_num += 1
    # print(one_channel_img.shape)
    # exit(0)
print(total_num)

# # 读取图像
# img = imageio.imread("lena.jpg")
#
# # 图像的尺寸通道h,w,c
# h,w,c = img.shape
#
# # 灰度计算公式
# gray = 0.2126*img[:,:,0] + 0.7152*img[:,:,1] + 0.0722*img[:,:,2]
#
# # 获得灰度图
# gray_img = gray.reshape(h,w).astype(np.uint8)
#
# # 保存结果
# imageio.imsave("Gray.jpg", gray_img)
