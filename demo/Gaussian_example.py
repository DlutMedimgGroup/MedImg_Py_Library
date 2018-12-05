"""
Script Name	  : Gaussian_example.py
Author		  : Han
Created		  : 2017/12/12
Version		  : 1.0
Description	  : gaussian filter
"""
import math
import numpy as np
from PIL import Image

# param input_image: the image that you want to process
# param size       : the size of gaussian kernel
# param sigma      : a param to get gassian kernel
# return           : the image which has been processed
def gaussian_filter(input_image, size, sigma):
    src = np.array(input_image)
    gaussian_kernel = _get_gaussiankernel(size, sigma)

    border = size // 2
    rows = src.shape[0] - 2 * border
    cols = src.shape[1] - 2 * border
    axis = len(src.shape)
    dst = src.copy()

    if axis == 2:
        for i in range(border, rows):
            for j in range(border, cols):
                k = 0
                for a in range(-border, border + 1):
                    for b in range(-border, border + 1):
                        k = k + gaussian_kernel[border + a, border
                                                + b] * src[i + a, j + b]
                dst[i, j] = k
        output_image = Image.fromarray(dst)
        return output_image

    if axis == 3:
        for i in range(border, rows):
            for j in range(border, cols):
                k = np.zeros(3)
                for a in range(-border, border + 1):
                    for b in range(-border, border + 1):
                        k = k + gaussian_kernel[border + a, border
                                                + b] * src[i + a, j + b, :]
                    a = a + 1
                dst[i, j, :] = k[:]
        output_image = Image.fromarray(dst)
        return output_image

# To get the gassian kernel
def _get_gaussiankernel(size, sigma):
    kernel = np.zeros((size, size))
    origin = size // 2
    sum = 0

    for i in range(size):
        x2 = (i - origin)**2
        for j in range(size):
            y2 = (j - origin)**2
            g = math.exp(-(x2 + y2) / (2 * sigma * sigma))
            sum = sum + g
            kernel[i, j] = g
    kernel = kernel / sum
    return kernel


if __name__ == '__main__':

    pic_src = Image.open('1.jpg')
    pic_dst = gaussian_filter(pic_src, 3, 1)
    pic_dst.save('hello.jpg')
