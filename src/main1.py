
#EXP 数据容器:列表list、元组tuple、字典dict、集合set

# list
list1=[1,2,3,4]
nestedList=[1,2,3,[4,5,6]]
# 下标访问
print(list1[-1])#-1表示最后一个元素
# print(list1[6])#如果下标越界，会报错ValueError: list index out of range
index = list1.index(3)#index()方法查找元素的下标

# 追加元素
list1.append(5)#append()方法在列表末尾添加一个元素
list1.extend([6,7])#extend()方法在列表末尾添加一个列表

# 删除元素
list1.remove(7)# remove()方法删除指定元素,会删除第一个匹配的元素
del list1[0]# del语句删除指定下标的元素
element = list1.pop(2)# pop(index)方法删除指定下标的元素,并且返回删除的元素

# count()方法统计元素出现的次数
print(list1.count(1))

# 其余方法和C++，java的语法类似，clear等

# 元组tuple是不可修改的list
tuple1 =(1,) # 如果只有一个元素，这个逗号必须有,否则类型不是tuple了

# 字符串也是不可修改
s5="123"
# s5[1]='9'#报错

# replace()
s5="Hello Niko and Niko's gun"
s6 = s5.replace("Niko","Simple")
print(s6)

# split()
s6 = s5.split(" ")
print(s6)

# strip()
s5 = "12Zywoo21"
s6 = s5.strip("12")
print(s6)

s5 = "  12Zywoo21  "
s6 = s5.strip()
print(s6)

# count() len() 没什么好说的

#EXP 切片 [开始:结尾:步长] 步长为负数表示反向
list1 = [1,2,3,4,5,6]
temp = list1[1:4]

#EXP 集合set 是无序的

set1 =set() # 空集合
set1 ={1,2,3,4,5,6}
temp = set1.pop() #随机取一个元素

set2 ={1,2,3,4,5,6}
set1.difference(set2)

set2.difference_update(set1) # set2去除交集

maxIndex =max(set2)

set1 ={1,2}
set2 ={3,4}
set3 = set1.union(set2)

#EXP 字典dict(就像C++的unordered_map) 存储键值对 可以嵌套(像json了，哈哈)
dict1 ={} # 空字典
dic1 = dict() # 空字典

dict1={"name":"niko", "age":18}
dict1["height"] =180
temp = dict1.keys()

#EXP 容器间可相互转换，就像使用构造函数

#EXP sorted()排序，返回列表，可以加一个reverse=True参数
print()
