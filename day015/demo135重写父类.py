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


demo1 = Demo1()
print(demo1.name)
print("==================================================")
demo2 = Demo2()
print(demo2.name)  # 222
# 完成了重写操作
