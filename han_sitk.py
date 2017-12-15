"""
Script Name	     : han_sitk.py
Author		     : Han
Created		     : 2017/12/15
Version		     : 1.0
Description	     : GaussianFilter in SimpleITK
"""
import SimpleITK as sitk


# param input_image: the image that you want to process
# param sigma      : a param to get gassian kernel
# return           : the image which has been processed
def gaussian_filter(input_image,sigma):
    _filter = sitk.SmoothingRecursiveGaussianImageFilter()
    _filter.SetSigma(sigma)
    return _filter.Execute(input_image)


if __name__ == '__main__':
    src_image = sitk.ReadImage('E:\\1.jpg')
    sitk.Show(src_image,"src_image")

    dst_image = gaussian_filter(src_image,5)
    sitk.Show(dst_image, "Gaussian")