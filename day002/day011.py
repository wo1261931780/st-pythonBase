# 下面是多个变量同时赋值
demo1, demo2, num1 = "11", "22", 33
# print(demo1 + "，demo1类型：" + type(demo1))
# 直接加号表示连接，后面是类型，不能直接相连
print(demo1 + "，demo1类型：", type(demo1))  # 11，demo1类型： <class 'str'>
print("==================================================")
num2 = num3 = 10
# print(num2 == num3, "，num2结果为："+ num2)  # 直接这样写也会报错
print(num2 == num3, "，num2结果为：", num2)  # True ，num2结果为： 10
