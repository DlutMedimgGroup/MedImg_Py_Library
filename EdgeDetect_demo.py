"""
  File name: EdgeDetect_demo
   Function：实现调用多个库的代码,使用边缘检测实现简单的线条画
    File No: 待定
 Created on: 2017-11-2
     Author: zengxiao
Modified on：217-1-14
     Author： zx
Description： 规范注释书写
"""

#-*- coding: utf8 -*-

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import xlsxwriter
import xlrd


img=Image.open('C:users/zengxiao/Desktop/ImageProcess/lena.jpg')    #使用PIL打开图片
makebw=np.array(img)                                                      #使用numpy得到像素矩阵
rows,cols,gre=makebw.shape                                                #使用numpy得到矩阵大小

#检测图像边缘

for x in range(rows-1):
    for y in range(cols-1):
        here=makebw[x,y]
        right=makebw[x+1,y]
        above=makebw[x,y+1]
        hereL=((here[0]+here[1]+here[2])/3)
        rightL=((right[0]+right[1]+right[2])/3)
        aboveL=((above[0]+above[1]+above[2])/3)
        if abs(hereL-rightL)>10 and abs(hereL-aboveL)>10:   #设置阈值10，像素变化速度的阈值
            makebw[x,y,0]=0
            makebw[x,y,1]=0
            makebw[x,y,2]=0
        if abs(hereL-rightL)<=10 and abs(hereL-aboveL)<=10:
            makebw[x,y,0]=255
            makebw[x,y,1]=255
            makebw[x,y,2]=255

#使用xlsxwriter将处理后的图像矩阵存入Excel文件中

file  = xlsxwriter.Workbook('C:/Users/zengxiao/Desktop/ImageProcess/LineDrawingMarrey.xlsx')    #创建Excel文件
sheet1 = file.add_worksheet('R')
sheet2 = file.add_worksheet('G')
sheet3 = file.add_worksheet('B')
for x in range(rows):
    for y in range(cols):
        sheet1.write(x, y, makebw[x,y,0])
        sheet2.write(x, y, makebw[x,y,1])
        sheet3.write(x, y, makebw[x,y,2])
file.close()

#使用xlrd从Excel中读取数据

data = xlrd.open_workbook('C:/Users/zengxiao/Desktop/ImageProcess/LineDrawingMarrey.xlsx')
table1 = data.sheets()[0]
table2 = data.sheets()[1]
table3 = data.sheets()[2]
nrows = table1.nrows
ncols = table1.ncols
remakebw=np.zeros((nrows,ncols,3))
for x in range(nrows):
    for y in range(ncols):
        remakebw[x,y,0] = table1.cell(x, y).value
        remakebw[x,y,1] = table2.cell(x, y).value
        remakebw[x,y,2] = table3.cell(x, y).value

#调用matplotible显示图像

makebwimg = Image.fromarray(makebw)
plt.figure('Line drawing')
plt.imshow(makebwimg)
plt.show()                                                                         #显示线条画图片
makebwimg.save('C:/Users/zengxiao/Desktop/ImageProcess/LineDrawing.jpg')    #存储线条画图片


