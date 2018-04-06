#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Script Name	  : ReadMhd_WriteOther
Author		  : ZengXiao
Created		  : 2018/4/5
Version		  : 1
Description	  :Convert Mhd to other format
"""
import SimpleITK as sitk

my_format = str(input('Enter a format you want to convert Mhd to : '))

src = sitk.ReadImage("D:\PythonCode\zx\src\PATIENT_DICOM.mhd")
img_array = sitk.GetArrayFromImage(src)
img = sitk.GetImageFromArray(img_array)

if my_format == 'nii':
    sitk.WriteImage(img, 'D:\PythonCode\zx\src\Result.nii')
elif my_format == 'nrrd':
    sitk.WriteImage(img, 'D:\PythonCode\zx\src\Result.nrrd')
else:
    print('Sorry, We do not support this format.\n')

