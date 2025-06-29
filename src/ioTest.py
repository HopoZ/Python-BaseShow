
#EXP 文件io
f =open('./source/test.txt','r+',encoding='UTF-8') # read write append对于三种文件权限 w会清空在重写 a指针在最后开始。加上+表示同时读取
a = f.read(5) #不带参数表示读取全部内容
print("a:",a)
b = f.readline()
print("b:",b)
c = f.readlines()
print("c:",c)

for line in f:
    print("for循环法",line.strip())


with open('./source/test.txt','r',encoding='UTF-8') as fileWith:
    print("这里的不需要close方法，出了代码块自动解除文件占用")

f.write("Hello")
f.flush() #这个会刷新文件，真正写入硬盘
f.close()