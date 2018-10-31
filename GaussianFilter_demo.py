"""
Script Name   :GaussianFilter_demo
Author        :zx
Created on    :2017/12/20
Last Modified :2017/12/20
Version       :1.0
Modifications :zx
Description   :调用SimpleITK实现Gaussian滤波
"""

import SimpleITK as sitk

#运用SimpleITK的函数读取图像
reader = sitk.ImageFileReader()
reader.SetFileName('C:users/zengxiao/Desktop/ImageProcess/lena1.jpg')
image = reader.Execute()

pixelID = image.GetPixelID()

gaussian = sitk.SmoothingRecursiveGaussianImageFilter()
gaussian.SetSigma(float(10))         #设置sigma值
image = gaussian.Execute(image)

caster = sitk.CastImageFilter()
caster.SetOutputPixelType(pixelID)
image = caster.Execute(image)

#存储高斯滤波后的图像
writer = sitk.ImageFileWriter()
writer.SetFileName('C:users/zengxiao/Desktop/ImageProcess/lena_Gaussian.jpg')
writer.Execute(image)
