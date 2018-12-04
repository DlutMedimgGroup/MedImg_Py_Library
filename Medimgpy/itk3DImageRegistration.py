#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Script Name	  : itk3DImageRegistration
Author		  : ZengXiao
Created		  : 2018/5/29
Version		  : 2.0
Description	  :
  PURPOSE     :
  INPUTS      : 3-D image registration
  - fix       : Path of fixed image
                Type of data: str
  - move      : Path of moving image
                Type of data: str
  - transform : Spatial Transform
                Type of data: str

                "euler": rigid transform
                "similarity": similarity transform
                "affine": affine transform
                "nonlinear": affine transform

  - metric    : Similarity Metric
                Type of data: str

                "information": Mutual Information
                "ANTS": Unknown
                "correlation": Normalized Cross Correlation
                "Hinformation": Joint Histogram Mutual Information
                "MeanSquares": Mean Squared Difference

  - interpolator: Optimizer
                  Type of data: str

                  "linear": Linear Interpolation
                  "nearest": Nearest Neighbor Interpolation
                  "BSpline": B-Spline Interpolation

  - optimizer  : Substitution value
                 Type of data: int

                 "AsGradient": Gradient Descendant
                 "StepGradient": Conjugate Gradient Descendant
                 "LBFGSB": LBFGSB
                 "LBFGS2": LBFGS2
                 "Exhaustive": Exhaustive
                 "Amoeba": Amoeba
                 "Weights": Weights
                 "Powell": Powell

   OUTPUTS    : None

"""
import SimpleITK as sitk
import os


def itk3DImageRegistration(fix, move, transform, metric, interpolator, optimizer):
    switch_SetTransform = {
        "euler": sitk.Euler3DTransform(fixed_image.GetDimension()),
        "similarity": sitk.Similarity3DTransform(fixed_image.GetDimension()),
        "affine": sitk.AffineTransform(fixed_image.GetDimension()),
        "nonlinear": sitk.BSplineTransform(fixed_image.GetDimension()),
    }
    switch_metric = {
        "information": registration_method.SetMetricAsMattesMutualInformation(numberOfHistogramBins=50),
        "ANTS": registration_method.SetMetricAsANTSNeighborhoodCorrelation(radius=50),
        "correlation": registration_method.SetMetricAsCorrelation(),
        "Hinformation": registration_method.SetMetricAsJointHistogramMutualInformation(numberOfHistogramBins=20,
                                                                                       varianceForJointPDFSmoothing=1.5),
        "MeanSquares": registration_method.SetMetricAsMeanSquares(),
    }
    switch_interpolator = {
        "linear": sitk.sitkLinear,
        "nearest": sitk.sitkNearestNeighbor,
        "BSpline": sitk.sitkBSpline,
    }
    switch_optimizer = {
        "AsGradient": registration_method.SetOptimizerAsGradientDescent(learningRate=1.0, numberOfIterations=100,
                                                                        convergenceMinimumValue=1e-6,
                                                                        convergenceWindowSize=10),
        "StepGradient": registration_method.SetOptimizerAsRegularStepGradientDescent(relaxationFactor=0.5,
                                                                                     gradientMagnitudeTolerance=1e-4,
                                                                                     maximumStepSizeInPhysicalUnits=0.0),
        "LBFGSB": registration_method.SetOptimizerAsLBFGSB(gradientConvergenceTolerance=1e-5, numberOfIterations=500,
                                                           maximumNumberOfCorrections=5,
                                                           maximumNumberOfFunctionEvaluations=2000,
                                                           maximumStepSizeInPhysicalUnits=0.0),
        "LBFGS2": registration_method.SetOptimizerAsLBFGS2(numberOfIterations=0, hessianApproximateAccuracy=6,
                                                           deltaConvergenceDistance=0, deltaConvergenceTolerance=1e-5,
                                                           lineSearchMaximumEvaluations=40, lineSearchMinimumStep=1e-20,
                                                           lineSearchMaximumStep=1e20, lineSearchAccuracy=1e-4),
        "Exhaustive": registration_method.SetOptimizerAsExhaustive(stepLength=1.0),
        "Amoeba": registration_method.SetOptimizerAsAmoeba(parametersConvergenceTolerance=1e-8,
                                                           functionConvergenceTolerance=1e-4),
        "Weights": registration_method.SetOptimizerWeights(),
        "Powell": registration_method.SetOptimizerAsPowell(numberOfIterations=100, maximumLineIterations=100,
                                                           stepLength=1,
                                                           stepTolerance=1e-6, valueTolerance=1e-6),
    }
    # read the images and casting the pixel type to Float32 (or Float64)
    fixed_image = sitk.ReadImage(fix, sitk.sitkFloat32)
    moving_image = sitk.ReadImage(move, sitk.sitkFloat32)

    # align the centers of the two volumes and set the center of rotation to the center of the fixed image.
    initial_transform = sitk.CenteredTransformInitializer(fixed_image,
                                                          moving_image,
                                                          switch_SetTransform.get(transform, 'Incorrect parameter input'),
                                                          sitk.CenteredTransformInitializerFilter.GEOMETRY)
    moving_resampled = sitk.Resample(moving_image, fixed_image, initial_transform,
                                     sitk.sitkLinear, 0.0, moving_image.GetPixelID())
    registration_method = sitk.ImageRegistrationMethod()

    # Similarity metric settings.
    switch_metric.get(metric, 'Incorrect parameter input'),
    registration_method.SetMetricSamplingStrategy(registration_method.RANDOM)
    registration_method.SetMetricSamplingPercentage(0.01)

    # Interpolator settings.
    registration_method.SetInterpolator(switch_interpolator.get(interpolator, 'Incorrect parameter input'))

    # Optimizer settings.
    switch_optimizer.get(optimizer,'Incorrect parameter input')

    registration_method.SetOptimizerScalesFromPhysicalShift()

    registration_method.SetOptimizerScalesFromPhysicalShift(centralRegionRadius=5,
                                                            smallParameterVariation=0.01)
    # Setup for the multi-resolution framework.
    registration_method.SetShrinkFactorsPerLevel(shrinkFactors=[4, 2, 1])
    registration_method.SetSmoothingSigmasPerLevel(smoothingSigmas=[2, 1, 0])
    registration_method.SmoothingSigmasAreSpecifiedInPhysicalUnitsOn()

    # Don't optimize in-place, we would possibly like to run this cell multiple times.
    registration_method.SetInitialTransform(initial_transform, inPlace=False)

    final_transform = registration_method.Execute(sitk.Cast(fixed_image, sitk.sitkFloat32),
                                                  sitk.Cast(moving_image, sitk.sitkFloat32))

    # Query the registration method to see the metric value and the reason the optimization terminated.
    print('Final metric value: {0}'.format(registration_method.GetMetricValue()))
    print('Optimizer\'s stopping condition, {0}'.format(registration_method.GetOptimizerStopConditionDescription()))
    sitk.WriteImage(moving_resampled, os.path.join('Output', 'D:\PythonCode\zx\src\moving.mhd'))
