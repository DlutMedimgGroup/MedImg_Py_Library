"""
 Script Name   : itkImageSmoothing
 Author		   : Boyce_Tian
 Created       : 2018/4/19
 Version       : 2.0
 Description   :
   PURPOSE     : Serving several ways to smooth the image
   INPUTS      :
   - image_arr : The array of the image you want to smooth.
   - type_str  :
     - DGauss  : Smooth image by function sitk.DiscreteGaussian()
     - Blur    : Smooth image by function sitk.BinomialBlur();
     - RGauss  : Smooth image by function sitk.RecursiveGaussian();
   OUTPUT      :
   - im_new    : An image as the result of smoothing.
"""

import SimpleITK as sitk

def itkImageSmoothing(Im_arr , type_str):

    # define the three ways
    func_1 = 'Discrete Gaussian'
    func_2 = 'Binomial Blurring'
    func_3 = 'Recursive Gaussian'

    #get an image from the array input
    image = sitk.GetImageFromArray(Im_arr)

    # find out the way to process the image according to type_str
    # smooth the image
    if type_str == func_1:

        im_new = sitk.DiscreteGaussian(image)

    elif type_str == func_2:

        im_new = sitk.BinomialBlur(image)

    elif type_str == func_3:

        im_new = sitk.RecursiveGaussian(image)

    else:
        print('Please check your spelling,'
              'and try again.')

    return im_new


# an example of using the function
# smooth an image by the 'Discrete Gaussian' and save the output
if __name__ == '__main__':
    impath = './src_image/CT159.dcm'
    im= sitk.ReadImage(impath)
    image_arr = sitk.GetArrayFromImage(im)
    image_new=itkImageSmoothing(image_arr ,'Discrete Gaussian')
    sitk.WriteImage(image_new,'./src_image/haha.dcm')