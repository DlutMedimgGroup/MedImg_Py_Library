#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Script Name	  : itkVectorFuzzyConnectednessImageFilter
Author		  : ZengXiao
Created		  : 2018/5/3
Version		  : 1.0
Description	  :
  PURPOSE     : I cannot find any Fuzzy Connectedness content in SimpleITK. I found function VectorConfidenceConnected
                which I think have the similar effects.
  INPUTS      :
  - image     : The path of image
                Type of data: str
  - seedList  : Seed
                Type of data: list
  - numberOFIterations: Number of iterations
                        Type of data: int
  - multiplier: Multiplier
                Type of data: float
  - initialNeighborhoodRadius: Initial neighborhood radius
                               Type of data: int
  - replaceValue: Substitution value
                  Type of data: int

   OUTPUTS    :
   - image    : Image


"""
import SimpleITK as sitk


def itkVectorFuzzyConnectednessImageFilter(path, seedList, iterations=4, multiplier=4.5, radius=1, replaceValue=1):
    img = sitk.GetArrayFromImage(sitk.ReadImage(path))
    result = sitk.VectorConfidenceConnected(img, seedList, iterations, multiplier, radius, replaceValue)
    return result

