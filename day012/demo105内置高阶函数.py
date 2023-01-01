list1 = [1, 2, 3, 66, 4, 54, 5]


def demo_run(num1):
    return num1 ** 2


result1 = map(demo_run, list1)  # map可以理解为，用指定的函数，处理指定的数据对象
print("==================================================")

print(result1)  # <map object at 0x000002C1999E9ED0>
print(list(result1))  # [1, 4, 9, 4356, 16, 2916, 25]
