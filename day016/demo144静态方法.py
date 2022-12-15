class Demo:
    def demo_run(self):
        print("我是demo中的运行方法")

    # 下面是静态方法
    @staticmethod
    def demo_run2(self):
        print("我是demo中的运行方法2")


print("==================================================")

demo1 = Demo()
demo1.demo_run()
demo1.demo_run2()
Demo.demo_run2()  # 静态方法也可以通过类调用
