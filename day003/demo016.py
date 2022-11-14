age = 1
while age != 0:
    age = int(input("请输入年龄："))
    if age < 18:
        print("too young")
    elif age <= 60:
        print("ok")
    else:
        print("too old")

print("finish")
