'''
Script Name	  : itkEdgePreservedSmoothing
Author         : Han
Created		  : 2018/4/21
Version		  : 1.0
Description	  : This is a function that smooth image with edge preserved.And
                 We provide following five types :
                 sitk.Bilateral( )
                 sitk.MinMaxCurvatureFlow( )
                 sitk.CurvatureFlow( )
                 sitk.CurvatureAnisotropicDiffusion( )
                 sitk.GradientAnisotropicDiffusion( )
'''


import SimpleITK as sitk


def itkEdgePreservedSmoothing(Im_arr, type_str): 
    '''
       input: Im_arr is the array of the image 
              type_str is the way you want to process      
       return: im_new which is an image as the result of smoothing.
       all functions used in this function are from SimpleITK
       here are the five functions got from SimpleITK to smooth image with edge
       preserved:
           sitk.Bilateral( )
           sitk.MinMaxCurvatureFlow( )
           sitk.CurvatureFlow( )
           sitk.CurvatureAnisotropicDiffusion( )
           sitk.GradientAnisotropicDiffusion( )
    '''
    # define the five ways
    func_1 = 'BilateralImageFilter'
    func_2 = 'MinMaxCurvatureFlowImageFilter'
    func_3 = 'CurvatureFlowImageFilter'
    func_4 = 'CurvatureAnisotropicDiffusionImageFilter'
    func_5 = 'GradientAnisotropicDiffusionImageFilter'


    #get an image from the array input
    image = sitk.GetImageFromArray(Im_arr)

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
# smooth an image by the 'Discrete Gaussian' and save the output
impath = '.\src_image\CT159.dcm'
image = sitk.ReadImage(impath,sitk.sitkFloat32)
image_arr = sitk.GetArrayFromImage(image)
image_new=itkEdgePreservedSmoothing(image_arr ,'CurvatureFlowImageFilter')
#sitk.WriteImage( image_new ,'.\src_image\out.dcm')