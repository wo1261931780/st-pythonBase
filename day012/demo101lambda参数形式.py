# demo_f1 = lambda demo1: 100
demo_f1 = lambda: 100
print(demo_f1())  # 没有参数，返回默认值的情况
print("==================================================")

demo_f2 = lambda demo1: demo1
print(demo_f2(55))  # 一个参数，返回参数本身
print("==================================================")

demo_f3 = lambda demo2, demo3: demo2 + demo3
print(demo_f3(100, 200))  # 300
print("==================================================")

demo_f4 = lambda demo4, demo5, demo6=100: demo4 + demo5 + demo6
print(demo_f4(1, 2))  # 103
print(demo_f4(11, 22, 33))  # 66
# 不指定的情况下，参数带有默认值的情况
print("==================================================")
demo_f5 = lambda *args: args
print(demo_f5(100, 200, 123, 132))
# (100, 200, 123, 132)
# 可变参数，返回的是一个元组类型的数据
print(demo_f5(11))  # (11,)
# 单个参数返回的也是元组类型的数据
print("==================================================")
demo_f6 = lambda **kwargs: kwargs
# print(demo_f6(100, 200, 123, 132))
print(demo_f6(name="11", age=22))
# {'name': '11', 'age': 22}
# 返回的是多个参数组合成的字典类型
