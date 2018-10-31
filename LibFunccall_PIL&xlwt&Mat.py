@version: python 3.3.0
@author: Mirabelle1
@lisenses: UTF-8
@see: Baidu
@note: to use the functions of the three libraries
@bug: can not find the path of the 'text.xls'
@attention: null


# param im_path: the path of the image
# param im:  the image
# param width, height: the width, height of the image
# rtype: int
# return: int(0)
# func:  to get the basic information like width, height of the image and save it.

from PIL import Image

im_path = r'C:\Users\lenovo\Desktop\11.jpg'
im = Image.open(im_path)
width, height = im.size

print(im.size, width, height)

print(im.format, im.format_description)
 
im.save(r'C:\Users\lenovo\Desktop\11.jpg')
im.show()


# param f: to build a new workbook
# param sheet1:  to save the data of the image in it
# param l_: the width, height of the image
# rtype: accounting to the list
# return: accounting to the list
# func:  to build a new workbook and  to save the data of the image in it.
import xlwt
f = xlwt.Workbook()
sheet1 = f,add_sheet(u'sheet1',cell_overwrite_=True)
l_=[im.size, width, height,im.format, im.format_description]
for i in range(len(l_)):
    sheet1.write(0,i,i)
f.save('text,xls')


# param x: Abscissa
# param y:  one of the ordinates 
# param z: the other ordinate
# param fig:to figure it
# rtype: float
# return: float
# func: To draw y=x^2(-3<=x<=3) and z=x*2(-3<=x<=3)

import matplotlib.pyplot as plt  
import numpy as np  
x = np.arange(-3,3.5,0.5)  
y = [ele**2 for ele in x]  
z = [ele *2 for ele in x]  
  
fig = plt.figure(1)  
  
ax = fig.add_subplot(211)  
line1 = ax.plot(x,y,'ro-')  
  
ax = fig.add_subplot(212)  
line2 = ax.plot(x,z,'g-')  
  
plt.show()  
