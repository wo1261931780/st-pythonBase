def show_me_system():
    print("-" * 20)
    print("1.添加学员")
    print("2.删除学员")
    print("3.修改学员")
    print("4.查询学员")
    print("5.显示所有学员")
    print("6.退出系统")
    print("-" * 20)


def input_order():
    customer_order = int(input("请输入命令："))
    return customer_order


common_classmate = []


def choose_order():
    while True:
        show_me_system()
        num = input_order()  # 执行输入过程
        if num == 1:
            print("添加学员")
            new_people = {"name": 1, "age": 1, "sex": 1, "number": 1}
            common_classmate.append(new_people)
        elif num == 2:
            print("删除学员")
            # 根据名称学号遍历，然后删除数组的内存地址
        elif num == 3:
            print("修改学员")
            # 根据名称学号遍历，然后修改字典
        elif num == 4:
            print("查询学员")
        elif num == 5:
            print("显示所有学员")
        elif num == 6:
            print("退出系统")
            break
        else:
            print("请重新输入")


choose_order()
print("==================================================")
