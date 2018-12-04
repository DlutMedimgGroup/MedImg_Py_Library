#title      :Tianzhihao_work3
#author     :Tianzhihao
#created    :20171108
#modified   :20171116
#description:draw a colored scatter by using python

import matplotlib.pyplot as plt
import numpy as ny
from PIL import Image

#生成随机数
a=ny.random.randint(55,1090,(100))
b=list(range(100))

#绘制随机数图像
plt.scatter(b,a,c=a,cmap=plt.cm.Reds,edgecolor='none',s=50)
plt.title("colored random number",fontsize=24)
plt.xlabel("random num",fontsize=14)
plt.ylabel("num",fontsize=14)
plt.show()
plt.savefig('randomnum.png',bbox_inches='tight')

#读取图像信息
im=Image.open("randomnum.png")
print(im.format,im.size,im.mode)
