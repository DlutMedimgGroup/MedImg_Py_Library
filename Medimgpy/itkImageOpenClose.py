import SimpleITK as sitk 
import numpy as np 

'''
Script name   :  itkImageOpenClose
Author        :  Hang Pan
Created       :  2018/05/03
Version       :  1.0
Description   :
	PURPOSE   :  Handle an image(support unsigned 8 integer) with opening or closing filter
	INCLUDING :
	- BinaryMorphologicalOpeningImageFilter
	- BinaryMorphologicalClosingImageFilter
	- OpeningByReconstructionImageFilter
	- ClosingByReconstructionImageFilter
'''


def BinaryMorphologicalOpeningImageFilter(filePath, finalPath):
	'''
	PURPOSE     : Handle an image(support unsigned 8 integer) with BinaryMorphologicalOpeningImageFilter
	INPUTS      : 
	- filePath  : Image file path
	- finalPath : Output image file path
	OUTPUT      : Handled image in the certain final path 
	'''

	itk_img = sitk.ReadImage(filePath, sitk.sitkUInt8)

	img_array = sitk.GetArrayFromImage(itk_img)
	print(img_array)
	print(type(img_array[0][0]))

	Obj = sitk.BinaryMorphologicalOpeningImageFilter()
	output = Obj.Execute(itk_img)
	sitk.WriteImage(output, finalPath)


def BinaryMorphologicalClosingImageFilter(filePath, finalPath):
	'''
	PURPOSE     : Handle an image(support unsigned 8 integer) with BinaryMorphologicalClosingImageFilter
	INPUTS      : 
	- filePath  : Image file path
	- finalPath : Output image file path
	OUTPUT      : Handled image in the certain final path 
	'''

	itk_img = sitk.ReadImage(filePath, sitk.sitkUInt8)

	img_array = sitk.GetArrayFromImage(itk_img)


	Obj = sitk.BinaryMorphologicalClosingImageFilter()
	output = Obj.Execute(itk_img)
	sitk.WriteImage(output, finalPath)

def OpeningByReconstructionImageFilter(filePath, finalPath):
	'''
	PURPOSE     : Handle an image(support unsigned 8 integer) with OpeningByReconstructionImageFilter
	INPUTS      : 
	- filePath  : Image file path
	- finalPath : Output image file path
	OUTPUT      : Handled image in the certain final path 
	'''

	itk_img = sitk.ReadImage(filePath, sitk.sitkUInt8)

	img_array = sitk.GetArrayFromImage(itk_img)
	print(img_array)
	print(type(img_array[0][0]))

	Obj = sitk.OpeningByReconstructionImageFilter()
	output = Obj.Execute(itk_img)
	sitk.WriteImage(output, finalPath)

def ClosingByReconstructionImageFilter(filePath, finalPath):
	'''
	PURPOSE     : Handle an image(support unsigned 8 integer) with ClosingByReconstructionImageFilter
	INPUTS      : 
	- filePath  : Image file path
	- finalPath : Output image file path
	OUTPUT      : Handled image in the certain final path 
	'''

	itk_img = sitk.ReadImage(filePath, sitk.sitkUInt8)

	img_array = sitk.GetArrayFromImage(itk_img)
	print(img_array)
	print(type(img_array[0][0]))

	Obj = sitk.ClosingByReconstructionImageFilter()
	output = Obj.Execute(itk_img)
	sitk.WriteImage(output, finalPath)


BinaryMorphologicalOpeningImageFilter('confirm.jpg','./3.jpg')
