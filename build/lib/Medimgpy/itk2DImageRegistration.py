"""
Script Name	  : itk2DImageRegistration
Author		  :
Created		  : 2018/5/31
Version		  : 1.0
Description   :
  PURPOSE     :
  INPUTS      :
  - Im_arr1   : fixed_image
                Type of data: not ndarray
  - Im_arr2   : moving_image
                Type of data: not ndarray
  - trans_type         : Spatial Transform algorithms
                        'Euler'       :  'Euler2DTransform'
                        'BSpline'     :  'BSplineTransformInitializer'
                        'Similarity'  :  'Similarity2DTransform'
                        'Affine'      :  'AffineTransform'
  - metric_type        : Similarity Metric algorithms
                        'mutual'      :  'SetMetricAsMattesMutualInformation'
                        'mean'        :  'SetMetricAsMeanSquares'
                        'correlation' :  'SetMetricAsCorrelation'
  - interpolator_type  : Interpolator algorithms
                        'Linear'      :  'sitkLinear'
                        'Neighbor'    :  'sitkNearestNeighbor'
                        'BSpline'     :  'sitkBSpline'
  - optimizer_type     : Optimizer algorithms
                        'GradientLine':  'SetOptimizerAsConjugateGradientLineSearch'
                        'LBFGSB'      :  'SetOptimizerAsLBFGSB'
                        'Powell'      :  'SetOptimizerAsPowell'
                        'Gradient'    :  'SetOptimizerAsGradientDescent'
   OUTPUTS    :
   - im_new   : Image

"""

import SimpleITK as sitk

def itk2DImageRegistration(Im_arr1,Im_arr2,trans_type,metric_type,interpolator_type,optimizer_type):
    # define the transform way
    tfunc_1 = 'Euler'
    tfunc_2 = 'BSpline'
    tfunc_3 = 'Similarity'
    tfunc_4 = 'Affine'

    mfunc1 = 'mutual'
    mfunc2 = 'mean'
    mfunc3 = 'correlation'

    ifunc1 = 'Linear'
    ifunc2 = 'Neighbor'
    ifunc3 = 'BSpline'

    ofunc1 = 'GradientLine'
    ofunc2 = 'LBFGSB'
    ofunc3 = 'Powell'
    ofunc4 = 'Gradient'



    # get an image from the array input
    fixed_image = sitk.GetImageFromArray(Im_arr1,)
    fixed_image = sitk.Cast(fixed_image, sitk.sitkFloat32)
    moving_image = sitk.GetImageFromArray(Im_arr2)
    moving_image = sitk.Cast(moving_image, sitk.sitkFloat32)

    # Spatial Transform algorithm depend on tfunc_ which are Euler,BSpline,Similarity,Affine
    if trans_type == tfunc_1:
        transform = sitk.CenteredTransformInitializer(fixed_image,
                                                      moving_image,
                                                      sitk.Euler2DTransform(),
                                                      sitk.CenteredTransformInitializerFilter.GEOMETRY)

    elif trans_type == tfunc_2:
        transform = sitk.BSplineTransformInitializer(fixed_image, [fixed_image.GetDimension(), 8])

    elif trans_type == tfunc_3:
        transform = sitk.CenteredTransformInitializer(fixed_image,
                                                      moving_image,
                                                      sitk.Similarity2DTransform(),
                                                      sitk.CenteredTransformInitializerFilter.GEOMETRY)

    elif trans_type == tfunc_4:
        transform = sitk.CenteredTransformInitializer(fixed_image,
                                                      moving_image,
                                                      sitk.AffineTransform(fixed_image.GetDimension()),
                                                      sitk.CenteredTransformInitializerFilter.GEOMETRY)

    # Similarity Metric algorithms depend on mfunc which are mutual information, mean squares, correlation
    registration_method = sitk.ImageRegistrationMethod()

    if metric_type == mfunc1 :
        registration_method.SetMetricAsMattesMutualInformation(numberOfHistogramBins=50)

    elif metric_type == mfunc2 :
        registration_method.SetMetricAsMeanSquares()

    elif metric_type == mfunc3 :
        registration_method.SetMetricAsCorrelation()

    registration_method.SetMetricSamplingStrategy(registration_method.RANDOM)
    registration_method.SetMetricSamplingPercentage(0.01)

    #Interpolator algorithm depends on ifunc which are Linear, Nearest neighbor, BSpline
    if interpolator_type == ifunc1:
        registration_method.SetInterpolator(sitk.sitkLinear)

    elif interpolator_type == ifunc2:
        registration_method.SetInterpolator(sitk.sitkNearestNeighbor)

    elif interpolator_type == ifunc3:
        registration_method.SetInterpolator(sitk.sitkBSpline)

    # Optimizer algorithms depends on ofunc which are Conjugate Gradient Line Search, LBFGSB, Powell, GradientDescen
    if optimizer_type == ofunc1:
        registration_method.SetOptimizerAsConjugateGradientLineSearch(learningRate=1.0, numberOfIterations=70)

    elif optimizer_type == ofunc2:
        registration_method.SetOptimizerAsLBFGSB()

    elif optimizer_type == ofunc3:
        registration_method.SetOptimizerAsPowell()

    elif optimizer_type == ofunc4:
        registration_method.SetOptimizerAsGradientDescent(learningRate=1.0, numberOfIterations=60)

    registration_method.SetOptimizerScalesFromPhysicalShift()

    registration_method.SetInitialTransform(transform)
    registration_method.Execute(fixed_image, moving_image)

    return transform

"""
  When the.py file is run directly, the code block under if __name__ = '__main__' is run.
  When the.py file is imported as a module, the code block under if __name__ = '__main__' is not run.
"""
if __name__ == '__main__':

#input, preprocessing and registration
    path1 = './src_image/CT_Head_Patient1.mhd'
    fixed_im = sitk.ReadImage(path1)
    fixed_image_arr = sitk.GetArrayFromImage(fixed_im)
    path2 = './src_image/MR_Head_Patient1.mhd'
    moving_im = sitk.ReadImage(path2)
    moving_image_arr = sitk.GetArrayFromImage(moving_im)
    transform = itk2DImageRegistration( fixed_image_arr, moving_image_arr,'BSpline','correlation','BSpline','Gradient')

    #resample and Rescale Intensity
    resampler = sitk.ResampleImageFilter()
    resampler.SetTransform(transform)
    resampler.SetReferenceImage(fixed_im)
    out = resampler.Execute(moving_im)
    img0 = sitk.Cast(sitk.RescaleIntensity(moving_im), sitk.sitkUInt8)
    img1 = sitk.Cast(sitk.RescaleIntensity(fixed_im), sitk.sitkUInt8)
    img2 = sitk.Cast(sitk.RescaleIntensity(out), sitk.sitkUInt8)
    img3 = sitk.Cast(sitk.RescaleIntensity(img1 / 2. + img2 / 2.), sitk.sitkUInt8)

    # combine these three scalar images into a multicomponent image named img_out
    img_out = sitk.Compose(img1, img2, img3)
    sitk.WriteImage(img_out,'./src_image/re_Head_Patient1.mhd')
