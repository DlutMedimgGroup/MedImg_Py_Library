#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Script Name   : hantaohai2.py
# Author        : Han
# Created       : 3 Nov 2017
# Last Modified	: 12 Nov 2017
# Description   : Using python to process experimental data

import xlrd
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from xlutils.copy import copy


path = "dawu.xls"        #excel文件地址
excel_rd = xlrd.open_workbook(path)  #打开excel
sheet_rd = excel_rd.sheet_by_index(0)   #sheet索引为1

m = sheet_rd.row_values(0)   #分别读入第1，2，3行
V1 = sheet_rd.row_values(1)
V2 = sheet_rd.row_values(2)

excel_wt = copy(excel_rd)
sheet_wt = excel_wt.get_sheet(0)
average=[]

for i in range(0,len(m)):
    ave = (V1[i]+V2[i])/2
    average.append(ave)
    sheet_wt.write(3,i,ave)
    excel_wt.save('dawu.xls')   #计算重复实验的平均值，并写入excel

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

# To display the result
plt.scatter(X,Y,color="red",label="Sample Point",linewidth=3) 
x=np.linspace(0,10,1000)
y=k*x+b
plt.plot(x,y,color="orange",label="Fitting Line",linewidth=2) 
plt.legend()
plt.show()
