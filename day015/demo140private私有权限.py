class Demo1:
    def __init__(self):
        self.name = "demo1"
        self.__age = 11  # 加了下划线，就是私有属性

    def demo_run1(self):
        print("我是demo1中的run1")

    def get_age(self):
        return self.__age

    def set_age(self):
        self.__age = 22
    # 在父类中定义获取方法和返回方法


class Demo2(Demo1):
    # def __init__(self):
    #     self.name = "demo2"

    def demo_run2(self):
        print("我是demo2中的run2")


print("==================================================")

demo1 = Demo2()
print(demo1.name)
# print(demo1.age)  # 因为是私有属性，所以无法直接访问
print(demo1.get_age())
demo1.set_age()
print(demo1.get_age())
