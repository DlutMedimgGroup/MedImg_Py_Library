"""
Script Name	  : itkImageLevelSetSegmentation
Author		  :
Created		  : 2018/5/3
Version		  : 1.2
Description   :
  PURPOSE     : Processing image using level-set segmentation
  INPUTS      :
  - Im_arr    : Im_arr is the array of the image
                Type of data: ndarray
  - type_str  : the type of image level-set segmentation that you want to process
                Type of data: str
                'SD'  :  'ShapeDetectionLevelSet'
                'GAC' ： 'GeodesicActiveContourLevelSet'
                'TH'  ： 'ThresholdSegmentationLevelSet'
                'FA'  ： 'FastMarching'
                'FAB' ： 'FastMarchingBase'
                'LP'  ： 'LaplacianSegmentationLevelSet'
   OUTPUTS    :
   - im_new   : Image
"""

import SimpleITK as sitk
import itkRegionGrow


def itkImageLevelSetSegmentation(Im_arr, type_str, seedlist=0):

    # define the six way
    func_1 = 'SD'
    func_2 = 'GAC'
    func_3 = 'TH'
    func_4 = 'FA'
    func_5 = 'FAB'
    func_6 = 'LP'

    # get an image from the array input
    image = sitk.GetImageFromArray(Im_arr)

    # find out the way to process the image according to type_str
    # smooth the image
    if type_str == func_1:
        image = sitk.Cast(image,sitk.sitkFloat32)
        image_pre=sitk.CannyEdgeDetection(image)
        im_new = sitk.ShapeDetectionLevelSet(image,image_pre)

    elif type_str == func_2:
        #image = sitk.GradientMagnitudeRecursiveGaussian(image)
        #featureImage = sitk.BoundedReciprocal(image)
        #seg = sitk.Image(image.GetSize(),sitk.sitkUInt8)
        #seg.CopyInformation(image)
        #seg[seedlist] = 1
        #distance = sitk.SignedMaurerDistanceMap(seg, insideIsPositive=True, useImageSpacing=True)
        #init_ls = sitk.BinaryThreshold(distance, -1000, 10)
        #init_ls = sitk.Cast(init_ls, featureImage.GetPixelID())*-1+0.5
        seg = itkRegionGrow.itkRegionGrow(Im_arr, 'CC', seedlist)
        init_ls = sitk.SignedMaurerDistanceMap(seg, insideIsPositive=True, useImageSpacing=True)
        im_new = sitk.GeodesicActiveContourLevelSet(init_ls, sitk.Cast(image, sitk.sitkFloat32))

    elif type_str == func_3:
        #seg = sitk.Image(image.GetSize(),sitk.sitkUInt8)
        #seg.CopyInformation(image)
        #seg[seedlist] = 1
        #seg = sitk.BinaryDilate(seg, 10)
        seg = itkRegionGrow.itkRegionGrow(Im_arr, 'CC', seedlist)
        stats = sitk.LabelStatisticsImageFilter()
        stats.Execute(image, seg)
        lower_threshold = stats.GetMean(1)-1.5*stats.GetSigma(1)
        upper_threshold = stats.GetMean(1)+1.5*stats.GetSigma(1)
        init_ls = sitk.SignedMaurerDistanceMap(seg, insideIsPositive=True, useImageSpacing=True)
        im_new = sitk.ThresholdSegmentationLevelSet(init_ls,sitk.Cast(image,sitk.sitkFloat32), lower_threshold, upper_threshold)

    elif type_str == func_4:
        im_new = sitk.FastMarching(image, seedlist)

    elif type_str == func_5:
        im_new = sitk.FastMarchingBase(image, seedlist)

    elif type_str == func_6:
        #seg = sitk.Image(image.GetSize(), sitk.sitkUInt8)
        #seg.CopyInformation(image)
        #seg[index] = 1
        #seg = sitk.BinaryDilate(seg, 8)
        seg = itkRegionGrow.itkRegionGrow(Im_arr, 'CC', seedlist)
        init_ls = sitk.SignedMaurerDistanceMap(seg, insideIsPositive=True, useImageSpacing=True)
        im_new = sitk.LaplacianSegmentationLevelSet(init_ls, sitk.Cast(image, sitk.sitkFloat32))

    else:

        print('Please check your spelling,'
              'and try again.')

    return im_new


# an example of using the function
if __name__ == '__main__':
    impath = './src_image/Result.nrrd'
    im = sitk.ReadImage(impath)
    seedlist = [[259, 158, 116]]
    image_arr = sitk.GetArrayFromImage(im)
    image_new = itkImageLevelSetSegmentation(image_arr, 'LP', seedlist)
    print(image_new.GetSize(), image_new.GetDimension(), image_new.GetPixelID())
    sitk.Show(image_new)
    image_out = sitk.Cast(image_new,sitk.sitkInt16)
    sitk.WriteImage(image_out, './src_image/hii.nrrd')