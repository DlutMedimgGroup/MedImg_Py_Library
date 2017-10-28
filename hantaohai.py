def h(x):       #计算阶乘的函数
    if x != 0:
        result=x*h(x-1)
    if x == 0:
        result=1
    return result

i = input("输入一个大于0的整数，计算它的阶乘：")

in_num=int(i)

print("它的阶乘为 %d" %h(in_num))
     