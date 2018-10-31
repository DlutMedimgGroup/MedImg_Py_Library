from __future__ import print_function
import SimpleITK as sitk
import sys
import os
if len ( sys.argv ) < 4:
    print( "Usage: %s <input> <sigma> <output>" % ( sys.argv[0] ) )
    sys.exit ( 1 )
image = sitk.ReadImage( sys.argv[1] )
pixelID = image.GetPixelID()
image  = sitk.SmoothingRecursiveGaussian( image,  float( sys.argv[2] ) )
sitk.WriteImage( sitk.Cast( image, pixelID ), sys.argv[3] )
