def demo_run(num1, num2, f):
    return f(num1) + f(num2)


print("==================================================")

# print(demo_run(1, -11, abs())) #直接这样会报错
print(demo_run(1, -11, abs))  # 相当于我第三个参数传递的是一个函数，然后返回的也是函数调用得到的数据
