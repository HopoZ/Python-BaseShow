s = "Hello, World!"

#EXP 打印数据类型 type() 查看的是数据的类型。变量(如"Hello, World!")是字面量，本身无类型，存储它的数据(如s)有类型
print(type(s))

#EXP 数据类型转换 int() float() str()
strM="11"

#strM里如果不是全是数字int()方法会发生错误
num_str=int(strM)
print(type(num_str),num_str)

float_str=float(strM)
print(type(float_str),str)

str2=str(num_str)
print(type(str2),str2)

#EXP 运算符 通用不用说。 /除 //整除 **指数 这是和C++,java不一样的。 赋值运算符也和C++，java一样

#EXP 字符串
s1='qwer'
s1="qwer"
s1="""q
w
e
r""" #三引号方式可以换行;如果没有变量接受这个三引号方式的字符串，就会被视为注释
print('-------------------------')

#EXP 字符串拼接 字符串格式化
s2="test%s"%s #使用%占位符
print('s2:'+s2)
s2=f"test{s}" #使用f"{}"
print('s2:'+s2)

s3="test%s %d"%(s,num_str)
print('s3:'+s3)
s3="test%s %s"%(s,num_str)#相当于发生了隐式转换int->string
print('s3:'+s3)

#EXP 格式化的精度控制 m.n m控制宽度，n控制小数位数
float_num=1.234
print('f:%6.2f' % float_num)

#EXP 输入
name=input("Tell me who are you\n") #input返回的是字符串类型
print(f"you are {name}")

#EXP 判断语法
if 10>11:
    print("10>11")
elif 10>9:
    print("10>9")
else:
    print("10<9")

i =0
while i<100:
    i+=1
    if i%2==0:
        continue
    print(i)

#EXP for循环的语法
name = 'abcd'
for i in name:
    print(i)

#EXP range()函数
for i in range(5):
    print(i)
for i in range(1,5):
    print(i)
for i in range(1,5,2):
    print(i)

#EXP 基础方面其余没什么与C++，java不一样的地方了
print('-------------------------')

#EXP 函数
def my_len(data):#默认是形参，按值引用
    """
    这是一个计算字符串长度的函数
    :param data: 字符串
    :return: 字符串长度
    """ #这是函数的文档注释，可以通过help(my_len)查看
    length=0
    for i in data:
        length+=1
    return length# 如果没有return语句，函数默认返回None，类型是NoneType,在if语句中会被视为False

s4 ="qwert"
print(my_len(s4))
help(my_len) #help()查看函数文档及函数定义位置

