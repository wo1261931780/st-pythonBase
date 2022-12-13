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


demo1 = Demo(11, 22)
demo1.demo_run()
print(demo1)  # 直接打印对象，有魔法方法存在的情况下
# 返回的就是方法中返回的说明文字
print("==================================================")
print(demo1.__str__())
