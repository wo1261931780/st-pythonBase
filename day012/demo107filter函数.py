list1 = [25, 12, 3, 2, 1, 35, 4]


def demo_run(num1):
    return num1 % 2 == 0


result1 = filter(demo_run, list1)
# filter实际上就是筛选器
# 简单来说，就是用参数1的函数，完成对指定数据的筛选
# 然后返回一个筛选后的结果
print(result1)  # <filter object at 0x0000020FCED59ED0>
print(list(result1))  # [12, 2, 4]
print("==================================================")
list2 = (1, 2, 3, 4, 5)
result2 = filter(demo_run, list2)
print(result2)
print(list(result2))  # [2, 4]
# 不管之前的数据是什么种类，最后返回的还是一个数组类型的结果
