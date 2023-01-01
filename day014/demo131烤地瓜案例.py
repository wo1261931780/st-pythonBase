class Demo:
    def __init__(self):
        self.condition = "raw"
        self.condiments = []
        self.time = 0

    def roast(self, time):
        if 0 < time < 10:
            self.condition = "waiting"
        elif time < 20:
            self.condition = "cooked"
        elif time >= 20:
            self.condition = "over cooked"
        else:
            self.condition = "raw"
        print(f"我是烤地瓜,当前状态为：{self.condition}")

    def tastes(self, condiments):
        self.condiments.append(condiments)
        print(f"我是调味料，当前调味料：{self.condiments}")

    def status(self, time):
        self.time += time
        print(f"我是地瓜状态，当前时间：{self.time}")
        self.roast(time)

    def __str__(self):
        return f"我是地瓜，我的状态：{self.condition}，我的时间：{self.time}，我的味道：{self.condiments}"


print("==================================================")
demo1 = Demo()
demo1.status(11)
print(demo1)
