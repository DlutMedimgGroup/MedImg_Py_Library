"""
  File name: AverageFilter_demo
   Function：实现模板滤波
 Created on: 2017-12-12
     Author: zx
"""

#-*- coding: utf8 -*-

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import xlsxwriter
import xlrd


img=Image.open('C:users/zengxiao/Desktop/ImageProcess/lena1.jpg').convert('RGB')    #使用PIL打开图片

radius = 1 ;    #模板的半径

#得到模板
sideLength = radius * 2 + 1
template = np.zeros((sideLength, sideLength))
for i in range(sideLength):
    for j in range(sideLength):
        template[i, j] = 1
all = template.sum()
template = template / all

#对图像进行滤波
arr = np.array(img)
height = arr.shape[0]
width = arr.shape[1]
newData = np.zeros((height, width))
for i in range(radius, height - radius):
    for j in range(radius, width - radius):
        t = arr[i - radius:i + radius + 1, j - radius:j + radius + 1]
        a = np.multiply(t, template)
        newData[i, j] = a.sum()
newImage = Image.fromarray(newData)

#显示滤波后的图像
plt.figure('模板滤波')
plt.imshow(newImage)
plt.show()



