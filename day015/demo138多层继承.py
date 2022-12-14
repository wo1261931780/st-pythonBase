class Demo1:
    def __init__(self):
        self.name = "demo1"

    def demo_run1(self):
        print("我是demo1的run1方法")


class Demo2(Demo1):
    def __init__(self):
        self.name = "demo2"

    def demo_run1(self):
        # print("我是demo2的run1方法")
        super().demo_run1()  # 我是demo1的run1方法
        # 跳过了方法重写，直接使用父类的run方法
        # super就是按照mro的顺序完成调用

    def demo_run2(self):
        print("我是demo2的run2方法")


class Demo3(Demo2):
    pass


print("==================================================")

show1 = Demo3()
show1.demo_run1()  # 我是demo2的run1方法
show1.demo_run2()  # 我是demo2的run2方法
