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


img=Image.open('E:\IMAGE-BME\ceshi.jpg') #打开图像并转化为数字矩阵
pix = img.load()
width = img.size[0]
height = img.size[1]

for i in range(1,width-1):
    for j in range(1, height-1):
        r1,g1,b1=pix[i-1,j-1]
        r2,g2,b2=pix[i-1,j]
        r3,g3,b3=pix[i-1,j+1]
        r4,g4,b4=pix[i,j-1]
        r5,g5,b5=pix[i,j]
        r6,g6,b6=pix[i,j+1]
        r7,g7,b7=pix[i+1,j-1]
        r8,g8,b8=pix[i+1,j]
        r9,g9,b9=pix[i+1,j+1]
        img.putpixel([i,j],((r1+r2+r3+r4+r5+r6+r7+r8+r9)/9,(g1+g2+g3+g4+g5+g6+g7+g8+g9)/9,(b1+b2+b3+b4+b5+b6+b7+b8+b9)/9))

img.show()
img.save("c.jpg")