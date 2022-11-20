demo_list = ["the", "money"]
print("==================================================")
demo_list.extend("demo")  # 这里是将字符串作为一个数组，拆分以后逐个追加进去
print(demo_list)  # ['the', 'money', 'd', 'e', 'm', 'o']
demo_list.extend(["show", "me"])
print(demo_list)  # ['the', 'money', 'd', 'e', 'm', 'o', 'show', 'me']
# 这里也是，有一层拆包的过程
# 先拆掉原始的数据类型，然后将其中的元素逐个添加到对象数据中
