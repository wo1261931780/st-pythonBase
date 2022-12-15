print("==================================================")


class Demo:
    __age = 11  # 私有类属性

    @classmethod
    def get__age(cls):  # 通过类方法，访问私有类属性
        return cls.__age


demo1 = Demo()
print(demo1.get__age())
