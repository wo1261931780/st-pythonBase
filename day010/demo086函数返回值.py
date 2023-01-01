def return_res():
    return 1, 2


print("==================================================")

print(return_res())  # (1, 2)
print(type(return_res()))  # <class 'tuple'>
# 在没有指定的情况下，返回的是元组类型的数据
# 如果有说明，就会返回指定的类型
