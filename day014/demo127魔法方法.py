print("==================================================")


class Demo:
    def __init__(self):  # 魔法方法，内置，具备一定的功能
        self.name = 123
        self.age = 222

    def demo_run(self):
        print("demo方法运行")
        print(self.name)
        print(self.age)


demo1 = Demo()
demo1.demo_run()
