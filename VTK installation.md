## 下载VTK的whl文件
VTK无法通过pip直接安装，需要下载对应Python版本的whl文件   
官网地址：https://www.vtk.org/download/  
国内镜像下载地址：https://www.lfd.uci.edu/~gohlke/pythonlibs/#vtk  
## 使用pip安装
在命令行窗口，cd到whl文件的目录下  
输入：pip install filename.whl
## 检验是否安装正确
在Python命令行中，输入：import vtk  
无报错，则vtk安装正确
## 注意
如无必要，请下载whl文件置本地，使用pip安装。  
使用别的安装方式，需要配置环境变量，而且极易出现python无法识别vtk模块名的情况，不推荐。
