print("==================================================")


class Demo1:
    def __init__(self):
        self.name = "111"

    def demo_run(self):
        print("我是demo1中的运行方法")


class Demo2(Demo1):
    pass
