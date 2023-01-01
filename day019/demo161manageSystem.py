import demo160students


class StudentManager:
    def __init__(self):
        self.student_list = []

    def manager_run(self):
        # 加载学员信息
        # self.load_student()
        while True:
            self.show_menu()
            menu_num = int(input("请输入需要执行的命令："))
            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.del_student()
            elif menu_num == 3:
                self.modify_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.show_student()
            elif menu_num == 6:
                self.save_student()
            elif menu_num == 7:
                self.exit_student()
                break
            else:
                # self.del_student()
                print("输入错误，请重新选择")

    @staticmethod
    def show_menu():
        print("==================================================")
        print("请选择如下功能：")
        print("1.添加学员")
        print("2.删除学员")
        print("3.修改学员")
        print("4.查询学员")
        print("5.展示学员")
        print("6.保存学员")
        print("7.退出系统")
        print("==================================================")

    def add_student(self):
        print("添加学员")
        tel = input("请输入手机号")
        name = input("请输入姓名")
        gender = input("请输入性别")
        age = input("请输入年龄")
        students1 = demo160students(name, gender, age, tel)
        self.student_list.append(students1)  # 通过内部类完成访问
        print(self.student_list)

    def del_student(self):
        print("删除学员")
        name = input("请输入姓名")
        for i in self.student_list:
            if i.name == name:
                self.student_list.remove(i)
                print("删除成功")
                break
        else:
            print("查无此人")
        print(self.student_list)

    def modify_student(self):
        print("修改学员")
        name = input("请输入姓名")
        for i in self.student_list:
            if i.name == name:
                i.tel = input("请输入手机号")
                i.name = input("请输入姓名")
                i.gender = input("请输入性别")
                i.age = input("请输入年龄")
                print("修改成功")
                break
        else:
            print("查无此人")
        print(self.student_list)

    def search_student(self):
        print("查询学员")

    def show_student(self):
        print("展示学员")
        try:
            text_io = open("demo163.txt", "r")
        except:
            text_io = open("demo163.txt", "w")
        else:
            text_io_read = text_io.read()
            eval1 = eval(text_io_read)
            self.student_list = [demo160students(i['name'], i['gender'], i['age'], i['tel']) for i in eval1]
        finally:
            text_io.close()

    def save_student(self):
        print("保存学员到文件")
        # 列表里面套字典
        text_io = open("demo163.txt", "w")
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)
        text_io.write(str(new_list))
        text_io.close()

    def exit_student(self):
        print("退出系统")
