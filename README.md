# MedImg_Py_Library
> A friendly starer guide and library for those who begins to learn medical image processing using Python.
We have starter guide manual and code resources for the beginners. The manual has two language versions: English and Chinese.
Created by the medical imaging group of Dalian univerisity of technology, China (http://biomedimg-dlut-edu.cn/)

Since the library is designed to help users process medical images easilier rather than create new ways to process them, we've written with reference to some existing open source libraries and some examples online.


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

# MedImg_Py_Library 中文README

> 对于那些刚开始使用Python学习医学图像处理的人来说，MedImg_Py_Library是一个友好的指南和函数库。

我们为初学者提供入门指南手册和代码资源。 
该手册有中英两种语言版本，由大连理工大学医学影像课题组创建，(http://biomedimg-dlut-edu.cn/)

由于该库旨在帮助用户更轻松地处理医学图像，而不是创建处理它们的新方法，因此我们参考了一些现有的开源库和一些在线示例。


## 下载源码

OS X & Linux & Windows:

```sh
git clone https://github.com/DlutMedimgGroup/MedImg_Py_Library.git
```

## 依赖

**MedImg_Py_Library** 需要如下几个依赖:

1. **python** v3.6 or higher
2. **SimpleITK** v1.1.0 or higher
3. **PyMesh** v0.2.1 or higher
4. **Numpy** v1.14.5 or higher
5. **Matplotlib** v2.2.2 or higher
6. **Pillow** v5.3.0 or higher
7. **vtk** v8.1.1 or higher

## 使用例子

首先，建立一个包含如下内容的Python的小脚本，并保存在某个路径下，命名为hello.py:

```py
import Medimgpy
import SimpleITK as sitk
impath = './src_image/CT159.dcm'   #the full path of your image
im = sitk.ReadImage(impath)
image_arr = sitk.GetArrayFromImage(im)
image_new = Medimgpy.itkImageSmoothing(image_arr ,'Discrete Gaussian')
sitk.WriteImage(image_new,'./src_image/haha.dcm')
```

切换你的当前路径到保存路径下

运行 *python3 hello.py*

## 文档

[中英文档][documents]

## 为本项目做贡献

1. Fork it (<https://github.com/DlutMedimgGroup/MedImg_Py_Library.git>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->

[documents]:<https://github.com/DlutMedimgGroup/MedImg_Py_Library.git>
