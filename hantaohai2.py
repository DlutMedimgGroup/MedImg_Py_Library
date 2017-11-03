#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#利用scipy和matplotlib对大学物理实验数据的处理，最小二乘法拟合并作图
#2017.11.3
#Author: Han
import xlrd
from xlutils.copy import copy
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

path = "dawu.xls"        #excel文件地址
data = xlrd.open_workbook(path)  #打开excel
table = data.sheet_by_index(0)   #sheet索引为0


file = copy(data)
sheet = file.get_sheet(0)


m =table.row_values(0)   #分别读入第1，2，3行
V1=table.row_values(1)
V2=table.row_values(2)

average=[]


for i in range(0,8):
    ave = (V1[i]+V2[i])/2
    average.append(ave)
    sheet.write(3,i,ave)
    file.save('dawu.xls')   #计算重复实验的平均值，并写入excel


X=np.array(m)
Y=np.array(average)         #将列表转变为矩阵，用scipy处理



def func(p, x):             #拟合目标函数
    k, b = p
    return k * x + b

def err(p,x,y):             #误差
    return func(p,x)-y


p0=[0,0]
out=optimize.leastsq(err,p0,args=(X,Y))     #用scipy的leastsq函数进行最小二乘法拟合
k,b=out[0]
print("k=",k,"b=",b)

plt.scatter(X,Y,color="red",label="Sample Point",linewidth=3) #画样本点
x=np.linspace(0,10,1000)
y=k*x+b
plt.plot(x,y,color="orange",label="Fitting Line",linewidth=2) #画拟合直线

plt.show()