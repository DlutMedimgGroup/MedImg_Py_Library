#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Script Name	  : itkImageEnhancement
Author		  : ZengXiao
Created		  : 2018/4/20
Version		  : 1.0
Description	  :
  PURPOSE     ：Enhance images with the function of SimpleITK
  INPUTS      :
  - path      : The path of the file which to be converted. Type of data: str
  - my_method : The methods of Image Enhancement. Type of data: str
  - method    :
    - GSD     : Gray scale Dilate
    - AHE     : Adaptive Histogram Equalization
    - LS      : Laplace Sharpening
  OUTPUT      : The enhanced image
  
"""
import SimpleITK as sitk


def itkImageEnhancement(path, my_method):
    # Define function itkImageEnhancement
    img = sitk.ReadImage(path)                  # Call SimpleITK to read the image
    result = []

    # img = sitk.HistogramMatching(img1, img2)  # 直方图匹配 Histogram Matching
    # 函数参数不一样，使用*args 出现error 尚未解决

    if my_method == 'GSD':                      # chose the method of enhancement
        result = sitk.GrayscaleDilate(img)      # save the file named result in the same path
        print('Gray Scale Dilate')              # Tell the user function worked successfully
    elif my_method == 'AHE':
        result = sitk.AdaptiveHistogramEqualization(img)
        print('Adaptive Histogram Equalization')
    elif my_method == 'LS':
        result = sitk.LaplacianSharpening(img)
        print('Laplace Sharpening')
    else:
        print('Error')   # Return an error

    return result


''' Test function '''
path = "D:/PythonCode/zx/src/a.dcm"            # Input path parameters
my_method = "AHE"                              # Method
image = itkImageEnhancement(path, my_method)   # Call function

my_method = "zx"
image = itkImageEnhancement(path, my_method)   # Try incorrect method
