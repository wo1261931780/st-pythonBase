dict1 = dict()
print(dict1)
print("==================================================")
dict2 = {i: i ** 2 for i in range(1, 5)}
print(dict2)  # {1: 1, 2: 4, 3: 9, 4: 16}
print("==================================================")
list1 = [1, 2, 3, 4, 5, 6, 6, 7]
list2 = [11, 22, 33, 44, 55, 66, 66, 997]

# dict3 = {list1[i]: list2[i] for i in range(len(list1))}
dict3 = {list1[i]: list2[i] for i in range(len(list1)) if len(list1) == len(list2)}
print(dict3)
# {1: 11, 2: 22, 3: 33, 4: 44, 5: 55, 6: 66, 7: 997}
# 将列表合并为字典的前提是：
# 两个列表的长度必须一致,否则字典会报错
