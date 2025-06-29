python的基础语法和一些常用的库与函数介绍，可点击关键字查看对应的代码示例。
# 基础



## 语法知识

### [输出 数据类型转换 运算符](./src/main.py)

### [数据容器:列表list、元组tuple、字典dict、集合set 数组切片](./src/main1.py)

### [函数的多返回值 函数的参数 类继承 生成器 装饰器 单例](./main2.py)

### [自创包的导入和使用](./src/packageTest)

### [文件IO](./src/ioTest.py)

### [异常处理](./src/exceptionTest.py)

# 使用python的一些可视化库

## textual
> 一个一个用于构建终端用户界面(TUI)的 Python 框架，它可以让开发者创建丰富、交互式的命令行应用程序。
### [textual构建时钟小程序](./src/textualTest.py)

- python -u textualTest.py来运行在命令行环境

![alt text](/images/image-1.png)

- 可运行textual serve "python -u textualTest.py"来运行在浏览器环境

![alt text](/images/image.png)

## echarts
### [生成数据对应折线图，保存为html对象](./src/commonPackageTest/pyechartsBase.py)

### [json格式解析和处理](./src/jsonTest.py)


# 使用python的一些网络编程库

## socket
> socket 模块提供了对底层网络接口的访问。
### [socket rich日志方案 同步+非阻塞](./src/networking/socket1.py)

    令HopoZ"惊喜"的是，你的控制台也无法通过ctrl+c来退出这个运行态，hhhh~
    socket通过setblocking(False)实现了非阻塞
    select实现同步等待事件(这一步会阻塞)，有事件会实现非阻塞态
