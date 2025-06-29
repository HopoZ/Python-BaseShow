python的基础语法和一些常用的库与函数介绍，可查看每个目录下对应的md文件
# 基础



## 语法知识

### [./main.py](./main.py)
- 输出 数据类型转换 运算符

### [./main1.py](./main1.py)
- 数据容器:列表list、元组tuple、字典dict、集合set 数组切片

### [./main2.py](./main2.py)
- 函数的多返回值 函数的参数

### [./packageTest](./packageTest)
- 包的导入和使用



# 使用python的一些可视化库

## textual
> 一个一个用于构建终端用户界面(TUI)的 Python 框架，它可以让开发者创建丰富、交互式的命令行应用程序。
### [.\textualTest.py](./textualTest.py)
- python -u textualTest.py来运行在命令行环境

![alt text](/images/image-1.png)

- 可运行textual serve "python -u textualTest.py"来运行在浏览器环境

![alt text](/images/image.png)

## echarts
### [./commonPackageTest/pyechartsBase.py](./commonPackageTest/pyechartsBase.py)
- 折线图保存为html对象

# 使用python的一些网络编程库

## socket
> socket 模块提供了对底层网络接口的访问。
### [./networking/socket1.py](./networking/socket1.py)
- rich日志方案

- 同步+非阻塞

    令人"惊喜"的是，你的控制台也无法通过ctrl+c来退出这个运行态，hhhh~
    socket通过setblocking(False)实现了非阻塞
    select实现同步等待事件(这一步会阻塞)，有事件会实现非阻塞态
