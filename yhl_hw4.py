"""
Script Name	      : mean_filter
Author		      : Yang HeLin
Created		      : 2017/12/11
Last Modified     : 2017/12/11
Version		      : 1
Modifications     :
Description	      : one kind of smoothing technique to remove
                    noise from an image
"""

#The "window" with 8 neighbors around slides over the image, and
# replacing each entry with the average of neighboring entries.
# param para1: 第一个参数的意义
# param para2: 第二个参数的意义
# param para3: 第三个参数的意义
# rtype:
# return:
# func:
#from skimage import data,io

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img=np.array(Image.open('E:\IMAGE-BME\ceshi.jpg'))  #打开图像并转化为数字矩阵
rows,cols,cha=img.shape
print(rows,cols,cha)
newimg=np.array([np.zeros((rows,cols)),np.zeros((rows,cols)),np.zeros((rows,cols))])
print(newimg.shape)
print(newimg)
A=[[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]
for k in {0,1,2}:
    for i in range(1,rows-1):
        for j in range(1,cols-1):
              a=sum(sum(img[i-1:i+2,j-1:j+2,k]*A))
              newimg[k,i,j]=(a)
             # print(a)
plt.imshow(newimg)
plt.axis('off')
plt.show()
