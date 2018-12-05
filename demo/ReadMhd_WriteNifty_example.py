'''
Script Name	  : ReadMhd_WriteNifty
Author		  : Boyce_Tian
Created		  : 2018/4/12
Version		  : 1.1
Description	  : a function named ReadMhd_WriteNifty which aims to transform image format from Mhd to Nifty
                input: impath is the path where your pending image is;
                       impath_new is the new path where you want the format changed image is;

'''

import SimpleITK as sitk

def ReadMhd_WriteNifty(impath,impath_new):

    '''
    input:param impath & impsth_new
    return: imsave which aim to save the format changed image to a new designated path;
    all functions used in this function are from SimpleITK
    sitk.ReadImage():aim to read the pending image in
    sitk.GetArrayFromImage():aim to get array from the image
    sitk.GetImageFromArray()&sitk.WriteImage():both achieve to write and save the new image as what we want

    '''

# main part of the function
    image=sitk.ReadImage(impath)
    image_arr=sitk.GetArrayFromImage(image)
    imnew=sitk.GetImageFromArray(image_arr)
    imsave=sitk.WriteImage(imnew,impath_new)
    return imsave

# an example of using the function
# read the new image in the format of Nifity
ReadMhd_WriteNifty('E:\python\PATIENT_DICOM.mhd',
                   'E:\python\PATIENT_DICOM.nii')
imnew_read=sitk.ReadImage('E:\python\PATIENT_DICOM.nii')
