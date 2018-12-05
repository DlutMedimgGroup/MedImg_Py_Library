from PIL import Image

im_path = r'C:\Users\lenovo\Desktop\11.jpg'
im = Image.open(im_path)
width, height = im.size

print(im.size, width, height)

print(im.format, im.format_description)
 
im.save(r'C:\Users\lenovo\Desktop\11.jpg')
im.show()

import matplotlib.pyplot as plt  
import numpy as np  
  
#To draw y=x^2(-3<=x<=3)  
  
x = np.arange(-3,3.5,0.5)  
y = [ele**2 for ele in x]  
z = [ele *2 for ele in x]  
  
fig = plt.figure(1)  
  
ax = fig.add_subplot(211)  
line1 = ax.plot(x,y,'ro-')  
  
ax = fig.add_subplot(212)  
line2 = ax.plot(x,z,'g-')  
  
plt.show()  