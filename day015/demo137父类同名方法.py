class Demo1:
    def __init__(self):
        self.name = "demo1"

    def demo_run(self):
        print("我是demo1类中的运行方法")

    def show_me(self):
        print("我是demo1中的show方法")


class Demo2:
    def __init__(self):
        self.name = "222"

    def demo_run2(self):
        print("我是demo2中的运行方法")


class Demo3(Demo1, Demo2):
    def __init__(self):
        self.name = "333"

    def make_cake(self):
        self.__init__()  # 先调用一个本类的初始化方法
        print("我是demo3中的cake方法")

    def make_demo1_cake(self):
        Demo1.__init__(self)
        # print("我是demo3中的demo1 cake方法")
        Demo1.demo_run(self)

    def make_demo2_cake(self):
        Demo2.__init__(self)  # 在子类中调用父类的初始化方法
        # print("我是demo3中的demo2 cake方法")
        Demo2.demo_run2(self)
        # 其实没有self也可以，但是调用的时候会报错


print("==================================================")
demo3 = Demo3()
demo3.make_cake()  # 我是demo3中的cake方法
demo3.make_demo1_cake()  # 我是demo1类中的运行方法
demo3.make_demo2_cake()  # 我是demo2中的运行方法
