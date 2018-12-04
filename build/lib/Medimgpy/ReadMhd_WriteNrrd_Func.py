import SimpleITK as sitk 
import numpy as np 


def ConvertToFormat(filePath, finalPath):
'''
;PURPOSE:
;	Definite a function that can input a img file and convert to an other curtain format img file.
;
;INPUT:
;	A img file path:     (*.mhd)
;	Other format path:   (*.nrrd, *nii)
;
;OUTPUT:
;	Other format in the input path.
;
;RETURN VALUE:
;	void
;
;AUTHER:
;	Hang Pan, Dalian University of Technology
;
;CREATION DATE:
;	2018-04-06
'''
	try:
		img = sitk.GetImageFromArray(sitk.GetArrayFromImage(sitk.ReadImage(filePath)))
	except Exception as e:
		print("ReadError: This file cannot be read!")

	try:
		sitk.WriteImage(img, finalPath)
	except Exception as e:
		print("FormatError: This format is not Support!")




if __name__ == '__main__':
	ConvertToFormat('PATIENT_DICOM.mhd', 'aaaaa.nrrd')

