list1 = [i for i in range(0, 10, 2)]
print(list1)
print("==================================================")
list2 = [i for i in range(10) if i % 2 == 1]
# 列表推导式的结构：
# 首先是需要保存的数据
# 然后是遍历方式
# 最后加一个if作为条件判断
print(list2)
