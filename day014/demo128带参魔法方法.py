print("==================================================")


class Demo:
    def __init__(self, name, age):  # 魔法方法有点类似于java中的构造方法
        self.name = name
        self.age = age
        # 但是，如果指定了带参数的魔法方法，就一定需要带参创建对象，否则报错

    def demo_run(self):
        print("demo方法运行")
        print(self.name)
        print(self.age)


demo1 = Demo(11, 22)
# 这里实际上就是带参构造
# 不需要你指定self本身存在
# 只要有参数，会按照顺序自动填充进去
demo1.demo_run()
