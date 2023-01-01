demo_list = ["the", "money"]
print(demo_list)
demo_list.append("test")  # 可以新增元素，代表列表是可变数据类型
print(demo_list)  # ['the', 'money', 'test']
print("==================================================")
demo_list.append([11, 22, 33])
print(demo_list)  # ['the', 'money', 'test', [11, 22, 33]]
print("==================================================")
show_me = [11, 22, 33, "123"]
demo_list.append(show_me)
print(demo_list)  # ['the', 'money', 'test', [11, 22, 33], [11, 22, 33, '123']]
# 这里往列表里面添加数据，是使用原始的数据直接作为对象添加，而不是添加一个对象的地址
print("==================================================")
