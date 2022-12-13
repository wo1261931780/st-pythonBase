class Demo:
    def __init__(self):
        self.height = None
        self.width = None

    def demo_run(self):
        print("demo类运行")
        print(self)
        self.width = 111
        self.height = 222
        # 在内部设置属性的时候，需要先进行初始化操作

    def show_me(self):
        print(f"我是运行类中的demo1.width属性{self.width}")
        print(f"我是运行类中的demo1.height属性{self.height}")
        # 不过，如果这样访问本身没有初始化的属性，也是可行的


demo1 = Demo()
demo1.demo_run()
# 可以在类外部设置对象属性
print(f"我是运行类中的demo1.width属性{demo1.width}")
print(f"我是运行类中的demo1.height属性{demo1.height}")
print("==================================================")
demo1.show_me()
