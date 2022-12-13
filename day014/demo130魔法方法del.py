class Demo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def demo_run(self):
        print("demo方法运行")
        print(self.name)
        print(self.age)

    def __str__(self):
        return "我是魔法方法str"

    def __del__(self):
        # return "demo del"
        print("对象已经删除")


demo1 = Demo(11, 22)
# demo1.demo_run()
demo1.__del__()
