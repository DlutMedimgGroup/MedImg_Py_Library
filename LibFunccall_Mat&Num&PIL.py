#应用三个库中函数的简单程序
#An example of using library functions
#田志浩 20171108

import matplotlib.pyplot as plt
import numpy as ny
a=ny.random.randint(55,1090,(100))
b=list(range(100))

plt.scatter(b,a,c=a,cmap=plt.cm.Reds,edgecolor='none',s=50)
plt.title("colored random number",fontsize=24)
plt.xlabel("random num",fontsize=14)
plt.ylabel("num",fontsize=14)
plt.show()
plt.savefig('randomnum.png',bbox_inches='tight')

from PIL import Image
im=Image.open("randomnum.png")
from __future__ import print_function
print(im.format,im.size,im.mode)
