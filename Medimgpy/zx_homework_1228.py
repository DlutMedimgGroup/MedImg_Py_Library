"""
Script Name   :zx_homework_1228
Author        :zx
Created on    :2017/12/28
Last Modified :2017/12/28
Version       :1.0
Modifications :zx
Description   :Demons图像变形配准
"""

from __future__ import print_function
import SimpleITK as sitk

def command_iteration(filter):
    print("{0:3} = {1:10.5f}".format(filter.GetElapsedIterations(),
                                     filter.GetMetric()))

fixed = sitk.ReadImage('C:users/zengxiao/Desktop/ImageProcess/lena1.jpg', sitk.sitkFloat32)

moving = sitk.ReadImage('C:users/zengxiao/Desktop/ImageProcess/lena10.jpg', sitk.sitkFloat32)

matcher = sitk.HistogramMatchingImageFilter()
matcher.SetNumberOfHistogramLevels(1024)
matcher.SetNumberOfMatchPoints(7)
matcher.ThresholdAtMeanIntensityOn()
moving = matcher.Execute(moving, fixed)

demons = sitk.DemonsRegistrationFilter()
demons.SetNumberOfIterations(50)
demons.SetStandardDeviations(1.0)

demons.AddCommand(sitk.sitkIterationEvent, lambda: command_iteration(demons))

displacementField = demons.Execute(fixed, moving)

print("-------")
print("Number Of Iterations: {0}".format(demons.GetElapsedIterations()))
print(" RMS: {0}".format(demons.GetRMSChange()))

outTx = sitk.DisplacementFieldTransform(displacementField)

#sitk.WriteTransform(outTx,'C:users/zengxiao/Desktop/ImageProcess/lenaDemons.jpg')

resampler = sitk.ResampleImageFilter()
resampler.SetReferenceImage(fixed);
resampler.SetInterpolator(sitk.sitkLinear)
resampler.SetDefaultPixelValue(100)
resampler.SetTransform(outTx)

out = resampler.Execute(moving)
simg1 = sitk.Cast(sitk.RescaleIntensity(fixed), sitk.sitkUInt8)
simg2 = sitk.Cast(sitk.RescaleIntensity(out), sitk.sitkUInt8)

cimg = sitk.Compose(simg1, simg2, simg1//2.+simg2//2.)
