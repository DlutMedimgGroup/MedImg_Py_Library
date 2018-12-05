"""
Script Name	      : yhl_171221
Author		      : Yang HeLin
Created		      : 2017/12/19
Last Modified     : 2017/12/19
Version		      : 1
Modifications     :
Description	      : one kind of smoothing technique to remove
                    noise from an image
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters

img=np.array(Image.open('yhl_pic.jpg'))  #打开图像并转化为数字矩阵

gaussimg = filters.gaussian_filter(img,sigma=2)

plt.figure()
plt.imshow(gaussimg)
plt.title('gaussian')
plt.axis('off')
plt.figure()
plt.imshow(img)
plt.title(u'original')
plt.axis('off')
plt.show()
