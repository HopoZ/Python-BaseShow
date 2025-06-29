
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

print("------------\n")
#EXP 类继承
class Animal:
    def sound(self):
        print("动物的声音")

class Dog(Animal):
    def sound(self):
        print("汪汪")

a = Dog()
a.sound() #汪汪
print("------------\n")
#EXP 生成器（Generator）
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # 暂停并返回当前值
        count += 1
# 使用for循环迭代生成器
for num in count_up_to(3):
    print(num)
print("------------\n")
#EXP 装饰器（Decorator）
def decorator(func):
    def wrapper():
        print("装饰器执行")
        func()
    return wrapper

@decorator
def my_function():
    print("函数执行")

my_function()
print("------------\n")
#EXP pyhon单例
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2) # true
print("------------\n")