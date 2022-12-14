class Demo1:
    def __init__(self):
        self.name = "demo1"

    def demo_run(self):
        print("我是demo1类中的demo方法")

    def show_me(self):
        print("我是demo1中的show方法")


class Demo2:
    def __init__(self):
        self.name = "222"

    def demo_run2(self):
        print("我是demo2中的运行方法")


class Demo3(Demo1):
    pass
    # 在不写任何方法的情况下，可以直接pass掉


class Demo4(Demo1, Demo2):
    pass
    # pass的同时，继承了所有的内容


print("==================================================")

demo1 = Demo4()
print(demo1.name)  # demo1
# 默认继承第一个父类中的属性
demo1.demo_run2()  # 但是不影响使用第二个父类的方法
