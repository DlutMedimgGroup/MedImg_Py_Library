"""
Script Name	      : yhl_171221
Author		      : Yang HeLin
Created		      : 2017/12/19
Last Modified     : 2017/12/19
Version		      : 2
Modifications     :
Description	      : one kind of smoothing technique to remove
                    noise from an image
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def conv2(img,fil):         
    
    fil_heigh = fil.shape[0]                        #获取卷积核(滤波)的高度
    fil_width = fil.shape[1]                        #获取卷积核(滤波)的宽度
    
    conv_heigh = img.shape[0] - fil_heigh + 1    #确定卷积结果的大小
    conv_width = img.shape[1] - fil_width + 1

    conv = np.zeros((conv_heigh,conv_width),dtype = 'uint8')
    
    for i in range(conv_heigh):
        for j in range(conv_width):                 #逐点相乘并求和得到每一个点
            conv[i][j] = wise_element_sum(img[i:i + fil_heigh,j:j + fil_width ],fil)
    return conv
    
def wise_element_sum(img,fil):          
    return (img * fil).sum()



img=np.array(Image.open('yhl_pic.jpg'))  #打开图像并转化为数字矩阵
rows,cols,cha=img.shape
print(rows,cols,cha)

A=np.ones([3,3])/9
newimg = []
for k in range(3):
    newimg.append(conv2(img[:,:,k],A))

newimg = np.dstack(newimg) 

plt.figure()
plt.imshow(img)
plt.title('original')
plt.axis('off')
plt.figure()
plt.imshow(newimg)
plt.title('Filtered renderings')
plt.axis('off')
plt.show()
