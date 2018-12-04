from PIL import Image

im_path = r'F:\Jupyter Notebook\csv_time_datetime_PIL\rabbit.jpg'
im = Image.open(im_path)
width, height = im.size

print(im.size, width, height)
print(im.format, im.format_description)

im.save(r'C:\Users\Administrator\Desktop\rabbit_copy.jpg')
im.show()
#读取文件

im = Image.open(im_path)
cropedIm = im.crop((700, 100, 1200, 1000))
cropedIm.save(r'C:\Users\Administrator\Desktop\cropped.png')
#裁剪图像
im = Image.open(im_path)
cropedIm = im.crop((700, 100, 1200, 1000))
im.paste(cropedIm, (0, 0))
im.show()
im.save(r'C:\Users\Administrator\Desktop\paste.png')
#复制粘贴