'''
Script Name	  : itkImageSmoothing
Author		  : Boyce_Tian
Created		  : 2018/4/19
Version		  : 1.0
Description	  : a function named itkImageSmoothing serves several ways to smooth the image.
                input: Im_arr is the array of the image you want to smooth
                       type_str is the name of which way you want to use to smooth image;
                       and there are three ways we provide:
                       'Discrete Gaussian','Binomial Blurring'and 'Recursive Gaussian'.
'''

import SimpleITK as sitk

def itkImageSmoothing(Im_arr , type_str):

    '''
       input:param Im_arr & type_str
             Im_arr is array
             type_str is character string
       return: im_new which is an image as the result of smoothing.
       all functions used in this function are from SimpleITK
       here are the three functions got from SimpleITK to smooth image:
       sitk.DiscreteGaussian();
       sitk.BinomialBlur();
       sitk.RecursiveGaussian();
    '''

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
impath = 'E:\python\CT159.dcm'
im= sitk.ReadImage(impath)
image_arr = sitk.GetArrayFromImage(im)
image_new=itkImageSmoothing(image_arr ,'Discrete Gaussian')
sitk.WriteImage(image_new,'E:\python\w11.dcm')