demo_exception = (NameError, FileNotFoundError, ZeroDivisionError)

try:
    text_io = open("demo146.txt", "r")
    print(1 / 0)
    print(demo)
except demo_exception as result:
    # 如果指定的异常，和实际发生的异常不一样，就不会指定这些代码
    # except (NameError, FileNotFoundError, ZeroDivisionError) as result:
    # 这里需要注意，使用的是元组类型的数据，保存异常类型
    # 使用元组保存数据，然后直接抛出元组类型的错误也是可以的
    print("我有异常，这里是异常后的代码")
    text_io = open("demo146.txt", "w")
    print(text_io)
    print(result)
    # 完整的报错提示：
    # FileNotFoundError: [Errno 2] No such file or directory: 'demo146.txt'
    # 实际打印的信息：
    # [Errno 2] No such file or directory: 'demo146.txt'

# print("==================================================")
# 如果存在多个报错信息，只会打印其中的一种
# division by zero
