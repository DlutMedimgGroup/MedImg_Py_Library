#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Script Name	  : ReadMhd_WriteNifty.py
Author		  : Han
Created		  : 2018/3/31
Version		  : 1.0
Description	  : ReadMhd_WriteNifty
"""
import SimpleITK as sitk

src = sitk.ReadImage("src_image/PATIENT_DICOM.mhd")
img_array = sitk.GetArrayFromImage(src)
img = sitk.GetImageFromArray(img_array)
sitk.WriteImage(img, 'src_image/Result.nii')
