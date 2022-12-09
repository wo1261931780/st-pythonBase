# 如果函数只有一个返回值，并且只有一句代码，就可以使用lambda表达式完成简化
def show_me():
    return 100


print(show_me())

print("==================================================")

result = lambda: 200
print(result)  # <function <lambda> at 0x0000029D6C7F00D0>
# 从这里可以看出来，lambda本质是一个函数
# 而这个函数是匿名的形式存在的
print(result())  # 因为本质是函数，所以使用函数的形式表达也是可以的
