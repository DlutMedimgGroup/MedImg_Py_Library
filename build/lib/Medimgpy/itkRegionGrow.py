"""
Script Name   : itkRegionGrow.py
Author        : Han
Created       : 2018/5/18
Version       : 1.0
Description   :
  PURPOSE     : This is a function which using the simplest segmentation approches,region growing
  INPUTS      :
  - im_arr    : Im_arr is the array of the image
                Type of data: ndarray
  - type_str  : the type of Region Grow that you want to process
                Type of data: str
                'CT'= 'ConnectedThreshold'
                'CC'= 'ConfidenceConnected'

   OUTPUTS    :
   - im_new   : Image
"""


import SimpleITK as sitk
import itkEdgePreservedSmoothing

def itkRegionGrow(im_arr, type_str, seedlist, lower=0, upper=1):

    func_1 = 'CT'
    func_2 = 'CC'

    # get an image from the array input
    image = itkEdgePreservedSmoothing.itkEdgePreservedSmoothing(im_arr, 'CF')
    image = sitk.GetImageFromArray(im_arr)
    image = sitk.Cast(image, sitk.sitkFloat32)

    # find out the way to process the image according to type_str
    if type_str == func_1:
        im_new = sitk.ConnectedThreshold(image, seedlist, lower, upper)

    elif type_str == func_2:
        im_new = sitk.ConfidenceConnected(image, seedlist)
    
    else:
        print('Please check your spelling,'
              'and try again.')
    return im_new


# an example of using the function
if __name__ == '__main__':

    impath = './src_image/CT159.dcm'
    image = sitk.ReadImage(impath)
    print(image.GetDimension(), image.GetPixelID(), image.GetPixelIDValue(), image.GetSize())
    image_arr = sitk.GetArrayFromImage(image)
    image_new = itkRegionGrow(image_arr, 'CC',[[271, 262, 0]],-50,50)
    print(image_new.GetDimension(), image_new.GetPixelID(), image_new.GetPixelIDValue(), image_new.GetSize())
    image_test = sitk.Cast(image_new, sitk.sitkInt16)
    print(image_test.GetDimension(), image_test.GetPixelID(), image_test.GetPixelIDValue(), image_test.GetSize())
    sitk.WriteImage(image_test, './src_image/yi.dcm')
    sitk.Show(image_test)