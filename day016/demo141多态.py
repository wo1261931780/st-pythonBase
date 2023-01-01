class Animal:
    def demo1(self):
        print("我是animal类中的demo1")


class Dog(Animal):
    def demo1(self):
        print("我是dog类中的demo1")

    def demo2(self):
        print("我是dog类中的demo2")


print("==================================================")

dog1 = Dog()
dog1.demo1()
dog1.demo2()
