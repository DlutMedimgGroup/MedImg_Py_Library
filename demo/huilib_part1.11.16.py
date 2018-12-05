import pylab as y    #引入pylab模块（pylab属于matplotlib的一个模块），并用y代替此模块

x = y.np.linspace(-10, 10, 100)  #设置x横坐标范围和点数，此为numpy中的，返回值为等间距的值
                                #numpy.linspace(a,b,c):a指的是开始位置，b表示的是结束位置，c表示产生点的个数（默认为50）

y.plot(x, x*x*x,'or')  #生成图像，此图像为y=x^3，后面加上‘o'表示为散点图
                        #'r'可设置颜色为红色

ax = y.gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')

ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')

ax.spines['left'].set_position(('data', 0))
ax.set_yticks([-1000, -500, 500, 1000])

y.xlim(x.min() , x.max() ) #将横坐标设置为x的最大值和最小值
y.show() #显示图像