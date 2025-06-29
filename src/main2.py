
#EXP 函数的多返回值
def test():
    return 1,2,3
x,y,z = test()

print()

#EXP 函数参数

#位置参数，根据函数参数位置传递参数
#关键字参数，使用key=value形式传参
#default参数，不传默认有值
#不定长参数 (会把参数合并为一个元组传入) *args参数个数不定长 **args进一步限定了参数必须是键值对形式
def test(**args):
    return 1,2,3
x,y,z = test()

#函数作为参数传递

#EXP 匿名函数 lambda 参数:处理 函数体只能写一行代码
