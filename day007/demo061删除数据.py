demo1 = {10, 11, 12}
demo1.remove(11)
print(demo1)  # {10, 12}
# demo1.remove(11) #如果数据不存在，就直接报错
# print(demo1)
print("==================================================")
demo1.discard(11)  # 同样是删除数据，如果数据不存在，也不会报错
print(demo1)
print("==================================================")
demo__pop = demo1.pop()  # 10
print(demo__pop)  # 删除一个随机数据，然后返回这个数据
