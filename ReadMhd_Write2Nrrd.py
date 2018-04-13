'''
 Script Name: ReadMhd_Write2Nrrd
 Author		: Helin Yang
 Created    : 2018/4/13
 Version    : 2
 Description:   This function is to convert only one image from the Mhd format to the Nrrd format.
                Given the full address of the image that needs to be converted as well as the
              full address of the new image.
                If run successfully, it prints out a completion statement to reminder you.
 '''

import SimpleITK as sitk


def ReadMhd_Write2Nrrd( mhd_full_path_name,nrrd_full_path_name):
   Image = sitk.ReadImage(mhd_full_path_name)
   image_array = sitk.GetArrayFromImage(Image)
   img = sitk.GetImageFromArray(image_array)
   sitk.WriteImage(img, nrrd_full_path_name)
   print ('The picture has been transferred.')

ReadMhd_Write2Nrrd('E:\IMAGE-BME\yanghelin\PATIENT_DICOM.mhd','E:\IMAGE-BME\yanghelin\PATIENT_DICOM.nrrd')