"""
Script Name	  : Watershed_example.py
Author		  : Han
Created		  : 2017/12/25
Version		  : 1.0
Description	  : actually，i don't know how it works
"""
import SimpleITK as sitk
import matplotlib.pyplot as plt


# param src        : the images that you want to plot
# description      : this is a function which can show the output image using matplotlib
def my_show(*args):
    for count, src in enumerate(args):
        nda = sitk.GetArrayViewFromImage(src)
        plt.subplot(1, len(args), count + 1)
        plt.imshow(nda)
    plt.show()


img = sitk.ReadImage('CT159.dcm', sitk.sitkFloat32)
img = img[:, :, 0]

feature_image = sitk.GradientMagnitude(img)
watershed_img = sitk.MorphologicalWatershed(feature_image,  markWatershedLine=True,
                                            fullyConnected=False, level=100)
my_show(img, feature_image, sitk.LabelToRGB(watershed_img))
