# 2018 Spring Semester Work Stage Summary

## Geometry Processing Library for Python

## Pymesh

Dependencies
PyMesh has the following required dependencies:

- Python v2.7 and v3.x.
- NumPy v1.8 or higher
- SciPy v0.13 or higher
- nose v1.3.7 or higher

The following C++ libraries are required. They are included in $PYMESH_PATH/third_party directory.

- Eigen v3.2 or higher
- PyBind11

PyMesh also has a number of optional dependencies:

- Carve: A fast, robust constructive solid geometry library.
- CGAL: The Computational Geometry Algorithms Library.
- Clipper: An open source freeware library for clipping and offsetting lines and polygons.
- Cork: A 3D boolean/CSG library.
- Draco: An open-source library for compressing and decompressing 3D geometric meshes and point clouds
- Geogram: A programming library of geometric algorithms
- libigl: A simple C++ geometry processing library.
- MMG: Robust, open source & multidisciplinary software for remeshing.
- Qhull: Engine for convex hulls, Delaunay triangulations, Voronoi diagrams computations.
- Quartet: A tetrahedral mesh generator that does isosurface stuffing with an acute tetrahedral tile.
- Tetgen: Tetrahedral mesh generation engine.
- Triangle: A two-Dimensional quality mesh generator and Delaunay triangulator.
- All of the optional libraries are included in $PYMESH_PATH/third_party directory.

PyMesh on GitHub: Website: https://github.com/qnzhou/PyMesh

PyMesh User Guide: http://pymesh.readthedocs.io/en/latest/user_guide.html

Recommend Python Library: Awesome Python https://awesome-python.com/#recommender-systems

## VTK

网上的资料有点旧了，试了下可以直接用下面的命令安装vtk-8.1.0,适用与Windows和Linux下

> pip install vtk

vtk 的帮助文档: https://www.vtk.org/doc/release/7.1/html/

## TVTK and mayavi 

介绍： http://docs.enthought.com/mayavi/tvtk/README.html#

The tvtk module (also called TVTK) provides a traits enabled version of VTK. TVTK objects wrap around VTK objects but additionally support traits, and provide a convenient Pythonic API. TVTK is implemented mostly in pure Python (except for a small extension module). Here is a list of current features.

1. All VTK classes are wrapped.
2. Classes are generated at install time on the installed platform.
3. Support for traits.
4. Elementary pickle support.
5. Pythonic feel.
6. Handles numpy arrays/Python lists transparently.
7. Support for a pipeline browser, ivtk and a high-level mlab like module.
8. Envisage plugins for a tvtk scene and the pipeline browser.
tvtk is free software with a BSD style license.

安装：

As of the latest release, i.e. 4.6.0 and above, if you are using Python 3.x and are on a 64 bit machine, installation via pip is the easiest and is as follows:

> $ pip install mayavi

> $ pip install PyQt5

Thats it!

## OpenGL

1.To find out some information about OpenGL:

Official website of OpenGL:https://www.opengl.org/

2.To instal OpenGL:

Download the installation package:https://pypi.org/project/PyOpenGL

Instal it as its prompts

3.Problems you may come across:

The download package is for 32bit machine

For more version:https://www.lfd.uci.edu/~gohlke/pythonlibs/

Find out the suitable one，do according to the above method.

4.If your machine is a 32bit one:

> $ pip install pyopengl 

It's the easiest way to instal it.
