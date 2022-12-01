print("==================================================")

help(len)
# len(obj, /)
#     Return the number of items in a container.
print("==================================================")


def add_total(num1, num2):
    """这里是说明文档"""
    demo = num1 + num2
    print(demo)


add_total(10, 20)
print("==================================================")
# help(add_total(10, 20))
# help(add_total(num1, num2))
# 上面两种方法都不能给出具体的说明，因为帮助只需要指定函数的名称即可
help(add_total)
# add_total(num1, num2)
#     这里是说明文档
print("==================================================")


def add_num(num1, num2):
    """
    这里可以写任意内容
    :param num1: 参数1
    :param num2: 参数2
    :return: 参数1+2的和
    """
    return num1 + num2
    # 多行注释，只需要在内部回车，就可以出现参数的提示信息


print("==================================================")
help(add_num)
# add_num(num1, num2)
#     :param num1: 参数1
#     :param num2: 参数2
#     :return: 参数1+2的和
