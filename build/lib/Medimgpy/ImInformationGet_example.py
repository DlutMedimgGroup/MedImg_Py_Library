from PIL import Image

im_path = r'C:\Users\lenovo\Desktop\11.jpg'
im = Image.open(im_path)
width, height = im.size

print(im.size, width, height)

print(im.format, im.format_description)
 
im.save(r'C:\Users\lenovo\Desktop\11.jpg')
im.show()

	
