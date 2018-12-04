"""
Script Name: ph_filter.py
Author: Panhang
Created: Build a template for filtering
Vertion: Python 3.6
Description: To build a template for filtering
"""

#param im: the array transformed by the image that you want to process
#param sigma: the para to get gaussian kernel
#return: the processed image


from PIL import Image
from pylab import *
from numpy import *
from scipy.ndimage import filters

#read the image and transform it into an array.
im = array(Image.open('C:/Users/lenovo/Desktop/test.jpg').convert('L'))

#To do gaussian filtering whichσ = 2.
im2 = filters.gaussian_filter(im,2)

#To do gaussian filtering whichσ = 5.
im3 = filters.gaussian_filter(im,5)

#To do gaussian filtering whichσ = 10.
im4 = filters.gaussian_filter(im,10)

gray()

#show the image
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
