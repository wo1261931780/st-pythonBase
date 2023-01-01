class Demo:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "我是搬家具"


class Home:
    def __init__(self, space, place):
        self.space = space
        self.remainingSpace = space
        self.place = place
        self.furnitureList = []

    def __str__(self):
        return f"我是房屋信息，总空间：{self.space}，剩余空间：{self.remainingSpace}，家具列表：{self.furnitureList}"

    def move(self, item):
        if item.area > self.remainingSpace:
            print("剩余空间不足")
        else:
            self.remainingSpace = self.space - item.area
            self.furnitureList.append(item)
            print(f"搬入成功，剩余空间为：{self.remainingSpace}")
            print(f"当前的家具列表为：{self.furnitureList}")
            if len(self.furnitureList) > 0:
                for i in self.furnitureList:
                    print(i.name)


print("==================================================")
demo1 = Demo("f1", 11)
demo2 = Demo("f2", 11)
home1 = Home(100, "jj")
home1.move(demo1)
