"""
Script Name   : itkEdgePreservedSmoothing
Author        : Han
Created       : 2018/5/3
Version       : 1.1
Description   :
  PURPOSE     : This is a function that smooth image with edge preserved
  INPUTS      :
  - im_arr    : Im_arr is the array of the image
                Type of data: ndarray
  - type_str  : the type of edge-preserved smoothing that you want to process
                Type of data: str
                'B'= 'BilateralImageFilter'
                'MC' = 'MinMaxCurvatureFlowImageFilter'
                'CF' = 'CurvatureFlowImageFilter'
                'CAD' = 'CurvatureAnisotropicDiffusionImageFilter'
                'GAD' = 'GradientAnisotropicDiffusionImageFilter'

   OUTPUTS    :
   - im_new   : Image
"""


import SimpleITK as sitk


def itkEdgePreservedSmoothing(im_arr, type_str):

    func_1 = 'B'
    func_2 = 'MC'
    func_3 = 'CF'
    func_4 = 'CAD'
    func_5 = 'GAD'

    # get an image from the array input

    image = sitk.GetImageFromArray(im_arr)
    image = sitk.Cast(image, sitk.sitkFloat32)

    # find out the way to process the image according to type_str
    # smooth the image
    if type_str == func_1:

        im_new = sitk.Bilateral(image)

    elif type_str == func_2:

        im_new = sitk.MinMaxCurvatureFlow(image)

    elif type_str == func_3:

        im_new = sitk.CurvatureFlow(image)

    elif type_str == func_4:

        im_new = sitk.CurvatureAnisotropicDiffusion(image)

    elif type_str == func_5:

        im_new = sitk.GradientAnisotropicDiffusion(image)

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
    image_new = itkEdgePreservedSmoothing(image_arr, 'GAD')
    print(image_new.GetDimension(), image_new.GetPixelID(), image_new.GetPixelIDValue(), image_new.GetSize())
    image_test = sitk.Cast(image_new, sitk.sitkInt16)
    print(image_test.GetDimension(), image_test.GetPixelID(), image_test.GetPixelIDValue(), image_test.GetSize())
    sitk.WriteImage(image_test, './src_image/yi.dcm')
