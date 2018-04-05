#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Script Name	  : ReadMhd_WriteNifty.py
Author		  : Hui
Created		  : 2018/4/05
Version		  : 1.0
Description	  : ReadMhd_Write2Nrrd
"""
import SimpleITK as sitk

src = sitk.ReadImage("PATIENT_DICOM.mhd")
img_array = sitk.GetArrayFromImage(src)
img = sitk.GetImageFromArray(img_array)
sitk.WriteImage(img, 'Result.nrrd')
