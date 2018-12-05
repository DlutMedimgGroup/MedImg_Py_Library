'''
Script Name	  : ReadMhd_Write_2_nrry
Author		  : libo_hui
Created		  : 2018/4/13
Version		  : 2.0
Description	  : a function named ReadMhd_Write_2_nrry which aims to transform image format from Mhd to nrry
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
    #src : target image
    #img_array : the array form image
    #img : the new created image what we want
    #imresult : return value
    src = sitk.ReadImage(impath)
    img_array = sitk.GetArrayFromImage(src)
    img = sitk.GetImageFromArray(img_array)
    imresult = sitk.WriteImage(img, impath_new)

    return imresult

# an example of using the function
# read the new image in the format of nrry
ReadMhd_WriteNifty('/Users/huilibo/PycharmProjects/test1/PATIENT_DICOM.mhd',
                   '/Users/huilibo/PycharmProjects/test1/Result_1.nrrd')
imnew_read=sitk.ReadImage('/Users/huilibo/PycharmProjects/test1/Result_1.nrrd')
