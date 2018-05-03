"""
 Script Name   : itkImageEdgeFiltering
 Author		   : Helin Yang
 Created       : 2018/4/19
 Version       : 3.0
 Description   :
   PURPOSE     : Compute the edge of the image 
   INPUTS      :
   - image_arr : The array of the image which to be converted.
   - method    :
     - Gass    : Computes the Magnitude of the Gradient of an image by convolution with the first derivative of a Gaussian.
     - Grad    : Computes the gradient magnitude of an image region at each pixel with a simple finite difference method.
   OUTPUT      : The edge of the image
"""
import SimpleITK as sitk

def itkImageEdgeFiltering(image_arr,method='Grad'):

    if method == 'Gass':
        sitk.GradientMagnitudeRecursiveGaussian(image_arr)
        print('Gradient Magnitude Recursive Gaussian')
    elif method == 'Grad':
        sitk.GradientMagnitude(image_arr)
        print('Gradient Magnitude')
    else:
        print('Error')



# An example
# Please don't forget to import those modules as follows
"""
import itkImageEdgeFiltering
import SimpleITK as sitk
image = sitk.ReadImage('E:\IMAGE-BME\yanghelin\PATIENT_DICOM.mhd')
image_new = itkImageEdgeFiltering.itkImageEdgeFiltering (image,'Gass')
sitk.WriteImage( image_new ,.\PATIENT_DICOM_new.mhd)
"""
