class Demo1:
    def __init__(self):
        self.name = "111"

    def demo_run(self):
        print("我是demo1中的运行方法")


class Demo2(Demo1):
    def __init__(self):
        self.name = "222"

    def demo_run2(self):
        print("我是demo2中的运行方法")


print("==================================================")
# 这里是使用类来调用功能，针对类的关系展示
print(Demo2.__mro__)  # 用来展示类之间的继承关系
# (<class '__main__.Demo2'>, <class '__main__.Demo1'>, <class 'object'>)
# demo2继承demo1，然后所有类都继承object类
