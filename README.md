# MedImg_Py_Library
> A friendly starer guide and library for those who begins to learn medical image processing using Python.
We have starter guide manual and code resources for the beginners. The manual has two language versions: English and Chinese.
Created by the medical imaging group of Dalian univerisity of technology, China (http://biomedimg-dlut-edu.cn/)

Since the library is designed to help users process medical images easilier rather than create new ways to process them, we've written with reference to some existing open source libraries and some examples online.

![](https://i.postimg.cc/0jwBLjQB/origin.jpg)
![](https://i.postimg.cc/mDqnXCb9/after.jpg)


## Download Source

OS X & Linux & Windows:

```sh
git clone https://github.com/DlutMedimgGroup/MedImg_Py_Library.git
```

## Dependencies

**MedImg_Py_Library** has the following required dependencies:

1. **python** v3.6 or higher
2. **SimpleITK** v1.1.0 or higher
3. **PyMesh** v0.2.1 or higher
4. **Numpy** v1.14.5 or higher
5. **Matplotlib** v2.2.2 or higher
6. **Pillow** v5.3.0 or higher
7. **vtk** v8.1.1 or higher

## Usage example

First create a small Python script called hello.py with the following content and save it somewhere:

```py
import Medimgpy
impath = './src_image/CT159.dcm'   #the full path of your image
im = sitk.ReadImage(impath)
image_arr = sitk.GetArrayFromImage(im)
image_new = Medimgpy.itkImageSmoothing(image_arr ,'Discrete Gaussian')
sitk.WriteImage(image_new,'./src_image/haha.dcm')
```

Change the directory to where your hello.py script can be found.

Run python3 hello.py

## Documents

[Documents][documents]

## Contributing

1. Fork it (<https://github.com/DlutMedimgGroup/MedImg_Py_Library.git>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request


<!-- Markdown link & img dfn's -->

[documents]:<https://github.com/DlutMedimgGroup/MedImg_Py_Library.git>
