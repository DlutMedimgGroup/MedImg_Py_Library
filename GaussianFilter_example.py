# -*- coding: utf-8 -*-

from PIL import Image

from pylab import *

from numpy import *

from scipy.ndimage import filters

#读取图片,灰度化并转为数组
im = array(Image.open('./test.jpg').convert('L'))

#进行σ = 2的高斯滤波
im2 = filters.gaussian_filter(im,2)

#进行σ = 5的高斯滤波
im3 = filters.gaussian_filter(im,5)

#进行σ = 10的高斯滤波
im4 = filters.gaussian_filter(im,10)

#显示图像
gray()

subplot(141)

title('source')

imshow(im)

subplot(142)

title('sigma=2')

imshow(im2)

subplot(143)

title('sigma=5')

imshow(im3)

subplot(144)

title('sigma=10')

imshow(im4)

show()

