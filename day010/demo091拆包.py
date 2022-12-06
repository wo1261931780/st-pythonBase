def ref_demo():
    return 100, 200


demo1, demo2 = ref_demo()
print(demo1)
print(demo2)
print("==================================================")
demo1 = (1, 234, 55)
demo3, demo4, demo5 = demo1  # 这就是拆包的过程
# 将一个元组拆分赋值到其它的变量中
print(demo3)
print(demo4)
print(demo5)
# print("==================================================")
# var1, var2 = demo1
# print(var1)
# 拆包要求数量必须匹配
