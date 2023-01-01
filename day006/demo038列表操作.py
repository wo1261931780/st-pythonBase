# 列表可以保存不同类型的数据
# 但是我们一般使用相同的数据类型，方便实际工作中操作数据

demo_list = ["demo1", "show", "junw", "the", "money"]
demo_list_join = "...".join(demo_list)
print(demo_list_join)
print(demo_list_join.find("junw"))
# 这里是一个简单应用，通过字符串拼接的方式找到数组中的元素是否存在指定字符串
print("==================================================")
print(demo_list[1])  # 根据索引去获取对应的元素
