demo_list = ["the", "money"]

print("==================================================")
demo_list.insert(1, "demo")  # 在指定索引开始添加
# 比如1号原来元素是demo1，插入demo2，
# 那么1号的元素目前就是demo2，原来的demo1变成2号元素
print(demo_list)  # ['the', 'demo', 'money']
print("==================================================")
del demo_list[1]  # 删除指定索引的元素
print(demo_list)  # ['the', 'money']
print("==================================================")
demo_list_pop = demo_list.pop(0)
print(demo_list)  # ['money'] ，原始列表也会发生改变
print(demo_list_pop)  # 返回被删除的元素
