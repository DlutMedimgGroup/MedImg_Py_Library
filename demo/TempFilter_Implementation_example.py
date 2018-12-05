"""
Script Name	  :im_filter
Author		  :Boyce_Tian
Created		  :20171213
Last Modified :
Version		  :1.0
Modifications :
Description	  :Implementation of template filtering
"""


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

Im=Image.open('E:\\python\\work4.jpg').convert('RGB')
arr_Im=np.array(Im)
width=arr_Im.shape[1]
height=arr_Im.shape[0]
#import the picture and turn it to a matrix

w_tem=3   #the width of template
for i in range(2,width-1):
    for j in range(2,height-1):
        arr=arr_Im[i-1:i+1,j-1:j+1]
        sumarr=np.sum(arr)
        arr_Im[i,j]=sumarr/(w_tem*w_tem)
output_Im=Image.fromarray(arr_Im)
#filtering processing

plt.imshow(output_Im)
plt.show()
