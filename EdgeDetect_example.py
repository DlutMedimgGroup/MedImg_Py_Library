"""
曾效的第二次作业
实现调用多个库的代码

Function：使用边缘检测创建简单的线条画

Created on: 2017-11-2
Author: zengxiao

"""
#-*- coding: utf8 -*-

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import xlsxwriter
import xlrd


img=Image.open('C:users/zengxiao/Desktop/ImageProcess/lena.jpg')     #使用PIL打开图片
makebw=np.array(img)                                                       #使用numpy得到像素矩阵
rows,cols,gre=makebw.shape                                                 #使用numpy得到矩阵大小

#检测图像边缘画出简单的线条画

for x in range(rows-1):
    for y in range(cols-1):
        here=makebw[x,y]
        right=makebw[x+1,y]
        above=makebw[x,y+1]
        hereL=((here[0]+here[1]+here[2])/3)
        rightL=((right[0]+right[1]+right[2])/3)
        aboveL=((above[0]+above[1]+above[2])/3)
        if abs(hereL-rightL)>10 and abs(hereL-aboveL)>10:                #设置阈值10，可改变
            makebw[x,y,0]=0
            makebw[x,y,1]=0
            makebw[x,y,2]=0
        if abs(hereL-rightL)<=10 and abs(hereL-aboveL)<=10:
            makebw[x,y,0]=255
            makebw[x,y,1]=255
            makebw[x,y,2]=255

#使用xlsxwriter将处理后的图像矩阵存入Excel文件中

file  = xlsxwriter.Workbook('C:/Users/zengxiao/Desktop/ImageProcess/LineDrawingMarrey.xlsx')
sheet1 = file.add_worksheet('R')
sheet2 = file.add_worksheet('G')
sheet3 = file.add_worksheet('B')
for x in range(rows):
    for y in range(cols):
        sheet1.write(x, y, makebw[x,y,0])
        sheet2.write(x, y, makebw[x,y,1])
        sheet3.write(x, y, makebw[x,y,2])
file.close()

data = xlrd.open_workbook('C:/Users/zengxiao/Desktop/ImageProcess/LineDrawingMarrey.xlsx')  # 读取xlsx文件
table1 = data.sheets()[0]               # 打开第一张表
table2 = data.sheets()[1]
table3 = data.sheets()[2]
nrows = table1.nrows
ncols = table1.ncols                    # 获取表的行数与列数

remakebw=np.zeros((nrows,ncols,3))

for x in range(nrows):                 #获取xlsx文件中存储的数据
    for y in range(ncols):
        remakebw[x,y,0] = table1.cell(x, y).value
        remakebw[x,y,1] = table2.cell(x, y).value
        remakebw[x,y,2] = table3.cell(x, y).value

makebwimg = Image.fromarray(makebw)
plt.figure('Line drawing')                                                       # 调用matplotilb工具显示图像
plt.imshow(makebwimg)
plt.show()
makebwimg.save('C:/Users/zengxiao/Desktop/ImageProcess/LineDrawing.jpg')    #保存图像


