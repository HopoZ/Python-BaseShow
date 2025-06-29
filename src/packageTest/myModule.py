def myAdd(x,y):
    print("my add func run")
    return x+y

if __name__ == '__main__': #防止测试代码在包被引用时自动执行
    myAdd(1,2)
__all__ =['myAdd'] #规定*代表的内容