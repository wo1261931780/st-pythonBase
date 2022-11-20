demo_list = ["demo1", "show", "junw", "the", "money"]

print(demo_list.index("the"))  # 3
# 数组的查询用法和字符串查询几乎完全一样
# print(demo_list.index("the", 0, 1))  # 没有结果的情况下，直接报错
print("==================================================")
print(demo_list.count("the"))  # 1
# print(demo_list.len())  #
print(len(demo_list))  # 数组长度5
print("==================================================")
print("demo" in demo_list)  # false
print("demo1" in demo_list)  # True
# 这里是用整个字符串作为元素来判断的
