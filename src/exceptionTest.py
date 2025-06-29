
#EXP 异常处理

#try except [else] [finally]关键字来处理，java里是try{}catch{}finally{}，没有else逻辑

#捕获指定异常
try:
    print(name)
except (NameError,ZeroDivisionError) as e: # Exception为异常顶级父类
    print(NameError,ZeroDivisionError)
else:
    print("没有异常")
finally:
    print("最后的处理")

#EXP 异常的传递性 函数本层未主动捕获异常会自动抛给上一层函数

