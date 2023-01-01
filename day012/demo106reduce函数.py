import functools

list1 = [1, 2, 3, 4, 5]


def demo_run(num1, num2):
    return num1 + num2


functools_reduce = functools.reduce(demo_run, list1)
# reduce的作用，是将带有两个参数的函数，做累积计算
# 这里的累积计算，是第一个参数和第二个参数计算一次，第二个和第三个计算一次，以此类推

print(functools_reduce)  # 15
print("==================================================")
list2 = [1]
print(functools.reduce(demo_run, list2))  # 1
# 这里可以看出来，函数对参数的数量没有具体的限制
# 换句话来说，如果我调用函数，处理的是只有一个参数的数据对象，也不会产生报错
