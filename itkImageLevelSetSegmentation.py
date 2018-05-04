"""
Script Name	  : itkImageLevelSetSegmentation
Author		  :
Created		  : 2018/5/3
Version		  : 1.0
Description	  : a function named itkImageLevelSetSegmentation serves several ways to segment the image by the level set method.
                input: Im_arr is the array of the image you want to segment
                       type_str is the name of which way you want to use to segment image;
                       and there are six ways we provide:
"""

import SimpleITK as sitk

def itkImageLevelSetSegmentation(Im_arr, type_str, index):

    """
       input:param Im_arr & type_str
             Im_arr is array
             type_str is character string
       return: im_new which is an image as the result of smoothing.
       all functions used in this function are from SimpleITK
       here are the three functions got from SimpleITK to smooth image:
       sitk.DiscreteGaussian();
       sitk.BinomialBlur();
       sitk.RecursiveGaussian();
    """

    # define the three ways
    func_1 = 'ShapeDetectionLevelSet'
    func_2 = 'GeodesicActiveContourLevelSet'
    func_3 = 'ThresholdSegmentationLevelSet'
    func_4 = 'FastMarching'
    func_5 = 'FastMarchingBase'
    func_6 = 'LaplacianSegmentationLevelSet'

    #get an image from the array input
    image = sitk.GetImageFromArray(Im_arr)
    #print(image.GetSize(),image.GetDimension(),image.GetPixelID())

    # find out the way to process the image according to type_str
    # smooth the image
    if type_str == func_1:
        image = sitk.Cast(image,sitk.sitkFloat32)
        image_pre=sitk.CannyEdgeDetection(image)
        im_new = sitk.ShapeDetectionLevelSet(image,image_pre)

    elif type_str == func_2:
        image = sitk.GradientMagnitudeRecursiveGaussian(image)
        featureImage = sitk.BoundedReciprocal(image)
        seg = sitk.Image(image.GetSize(),sitk.sitkUInt8)
        seg.CopyInformation(image)
        seg[index]=1
        #seg = sitk.BinaryDilate(seg,1)
        distance= sitk.SignedMaurerDistanceMap(seg,insideIsPositive=True,useImageSpacing=True)
        init_ls = sitk.BinaryThreshold(distance,-1000,10)
        init_ls = sitk.Cast(init_ls,featureImage.GetPixelID())*-1+0.5
        #print(init_ls.GetSize(),init_ls.GetDimension())
        im_new = sitk.GeodesicActiveContourLevelSet(init_ls,featureImage)

    elif type_str == func_3:
        seg = sitk.Image(image.GetSize(),sitk.sitkUInt8)
        seg.CopyInformation(image)
        seg[index]=1
        seg = sitk.BinaryDilate(seg,10)
        stats = sitk.LabelStatisticsImageFilter()
        stats.Execute(image,seg)
        #print(stats)
        lower_threshold = stats.GetMean(1)-1.5*stats.GetSigma(1)
        upper_threshold = stats.GetMean(1)+1.5*stats.GetSigma(1)
        #print(lower_threshold,upper_threshold)
        init_ls = sitk.SignedMaurerDistanceMap(seg,insideIsPositive=True,useImageSpacing=True)
        #print(init_ls.GetSize(),init_ls.GetDimension())
        im_new = sitk.ThresholdSegmentationLevelSet(init_ls,sitk.Cast(image,sitk.sitkFloat32),lower_threshold,upper_threshold)

    elif type_str == func_4:
        im_new = sitk.FastMarching(image, [[223, 440, 0], [223, 442, 0]])

    elif type_str == func_5:
        im_new = sitk.FastMarchingBase(image, [[223, 440, 0], [223, 442, 0]])

    elif type_str == func_6:
        seg = sitk.Image(image.GetSize(), sitk.sitkUInt8)
        seg.CopyInformation(image)
        seg[index] = 1
        seg = sitk.BinaryDilate(seg, 8)
        init_ls = sitk.SignedMaurerDistanceMap(seg, insideIsPositive=True, useImageSpacing=True)
        im_new = sitk.LaplacianSegmentationLevelSet(init_ls, sitk.Cast(image, sitk.sitkFloat32))

    else:

        print('Please check your spelling,'
              'and try again.')

    return im_new


# an example of using the function
#
impath = './src_image/PATIENT_DICOM.nrrd'
im = sitk.ReadImage(impath)
index = (248, 223, 13)
image_arr = sitk.GetArrayFromImage(im)
image_new = itkImageLevelSetSegmentation(image_arr, 'LaplacianSegmentationLevelSet', index)
print(image_new.GetSize(), image_new.GetDimension(), image_new.GetPixelID())
sitk.Show(image_new)
image_out = sitk.Cast(image_new,sitk.sitkInt16)
sitk.WriteImage(image_out, './src_image/hii.nrrd')
