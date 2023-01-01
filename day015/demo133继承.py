class Demo1:
    def demo_run1(self):
        print("我是demo1中的运行类")


class Demo2(object):  # 如果没有继承类，默认继承object类
    def demo_run2(self):
        print("我是demo2中的运行类")


# 这也是经典类和新式类的区别
class Demo3(Demo1):  # demo3继承demo1
    def demo_run3(self):
        print("我是demo3中的运行类")


print("==================================================")

demo3 = Demo3()
demo3.demo_run3()
demo3.demo_run1()
# 和java一样，继承以后就会获得父类中的所有方法
