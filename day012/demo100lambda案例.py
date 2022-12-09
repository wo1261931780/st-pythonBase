def demo_run(num1, num2):
    return num1 + num2


print("==================================================")

result = demo_run(1, 2)
print(result)
print("==================================================")
demo_result = lambda demo1, demo2: demo1 + demo2
print(demo_result)  # <function <lambda> at 0x000001D9328A00D0>
print(demo_result(1, 3))  # 4
# 上面这种打印的是函数的内存地址
# 因为只是单纯打印了函数，没有给变量赋值，再简单点说，就是没有完成函数调用
# 下面的才会打印具体的函数返回结果
print("==================================================")
