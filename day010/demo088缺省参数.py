def demo_run(name1, age1, gender1="male"):
    print(f"姓名是：{name1}，年龄：{age1}，性别：{gender1}")


print("==================================================")
demo_run(11, 22, 33)
demo_run(11, 22)  # 姓名是：11，年龄：22，性别：male
# 没有指定的情况下，使用的缺省参数
