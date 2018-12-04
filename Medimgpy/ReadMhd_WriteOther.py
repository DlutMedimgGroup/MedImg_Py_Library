#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Script Name	  : ReadMhd_WriteOther
Author		  : ZengXiao
Created		  : 2018/4/5
Modified      : 2018/4/7
Version		  : 2.0
Description	  :
PURPOSE：
    Convert Mhd to nii and nrrd format.

INPUTS:
    path: The path of the file which to be converted.
        Type of data: str
    my_format: The format we want to convert to.
        Type of data: str

RETURNED VALUE:
    The converted file named 'result' in the same path.

Modified :
    Add notes and rewritten the nodes as function.

"""
import SimpleITK as sitk


def format_conv(path, my_format):
    # Define function format_conv
    src = sitk.ReadImage(path)                  # Call SimpleITK to read the image
    img_array = sitk.GetArrayFromImage(src)     # Convert image to array
    img = sitk.GetImageFromArray(img_array)     # Convert array to image

    # Get the path the file located
    l = len(path)
    for i in range(0, l):
        if path[l - 1 - i] == '\\':       # Find the last \
            end = l - i
            break

    self_path = path[0:end]              # Get the path of file

    if my_format == 'nii':                                  # chose which format to save
        sitk.WriteImage(img, self_path + 'result.nii')      # save the file named result in the same path
        print('format_conv')                                # Tell the user function worked successfully
    elif my_format == 'nrrd':
        sitk.WriteImage(img, self_path + 'result.nrrd')
        print('format_conv')
    else:
        print('Sorry, We do not support this format.')   # If there is an unexpected format, inform the error


''' Test function '''
path = "D:\PythonCode\zx\src\PATIENT_DICOM.mhd"     # Input path parameters
my_format1 = "nii"              # Input format parameters
format_conv(path, my_format1)   # Call function

my_format2 = "nrrd"             # Try another format
format_conv(path, my_format2)

my_format3 = "txt"              # Try false format
format_conv(path, my_format3)