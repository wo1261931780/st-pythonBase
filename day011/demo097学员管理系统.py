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


def query_classmate_info(new_people, num):
    """
    传递字典,查询所有学员数据
    :param new_people: dict
    :return: boolean
    """
    if isinstance(new_people, dict):
        if len(common_classmate) == 0:
            return True
        else:
            for i in common_classmate:
                if i.get("name") == new_people.get("name") and i.get("age") == new_people.get("age"):
                    print("学员存在")
                    return False
                elif i.get("number") == new_people.get("number"):
                    if num == 2: common_classmate.remove(new_people)
                    return True
                else:
                    new_people["number"] = 123456  # 新增的时候，会默认随机一个学号出来
                    print("新增成功")
                    return True
    else:
        return False


def input_info(flock):
    """
    将整个输入模块抽象出来
    根据参数值设置输入的内容
    :param flock: 模块
    :return: 返回一个带着参数的字典
    """
    new_people = {"name": 1, "age": 1, "sex": 1, "number": 1}
    input_name = input("请输入姓名：")
    new_people["name"] = input_name
    input_age = input("请输入年龄：")
    new_people["age"] = input_age
    if flock == 4 and flock == 2: return new_people  # 查询学员，不需要输入后面的内容
    input_sex = input("请输入性别：")
    new_people["sex"] = input_sex
    return new_people


def choose_order():
    while True:
        show_me_system()
        num = input_order()  # 执行输入过程
        if num == 1:
            print("添加学员")
            new_people = input_info(num)
            if query_classmate_info(new_people):
                common_classmate.append(new_people)
                print("添加完成")
                print(common_classmate)
                print("==================================================")
        elif num == 2:
            print("删除学员")
            new_people = input_info(num)
            if query_classmate_info(new_people):
                print("删除成功")
                print(common_classmate)
            # 根据名称学号遍历，然后删除数组的内存地址
            else:
                print("学号不存在，删除失败")
        elif num == 3:
            print("修改学员")
            # 根据名称学号遍历，然后修改字典
        elif num == 4:
            print("查询学员")
            # 模糊查询
        elif num == 5:
            print("显示所有学员")
            print(common_classmate)
        elif num == 6:
            print("退出系统")
            break
        else:
            print("请重新输入")


choose_order()
print("==================================================")
