list1 = [11, 22, 33, 44, 55, 55, 11]
set1 = {1, 2, 3, 4, 5, 6}
tuple1 = ("demo1", "demo2", "demo3", "demo4")
print(list1)
print(type(list1))
print(type(tuple(list1)))  # <class 'tuple'>
# 直接设置一个类型就可以完成转换
print("==================================================")
print(type(set(list1)))  # <class 'set'>
print(list1)  # 这里好像没有完成去重操作
print("==================================================")
print(type(str(list1)))  # <class 'str'>
print(list1)  # [11, 22, 33, 44, 55]
# 转换为字符串以后，格式不会发生变化
print("==================================================")
demo = "demo"
# print(type(dict("demo"))) # 转换字典类型会出现错误
print(type(set(demo)))
print(demo)
