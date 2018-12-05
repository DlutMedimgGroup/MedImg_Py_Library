from PIL import Image
im = Image.open('ceshi.JPG')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('suoxiao.jpg', 'JPEG')
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)
plt.figure(figsize=(8,4))
plt.plot(x,y,label="sin(x)",color="red",linewidth=2)
plt.plot(x,z,"b--",label="cos(x^2)")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("First Example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()