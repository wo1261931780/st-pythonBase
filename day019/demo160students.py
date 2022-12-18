class Student:
    def __init__(self, name, gender, age, tel):
        self.age = age
        self.tel = tel
        self.name = name
        self.gender = gender

    def __str__(self):
        return f"我是学员信息，姓名：{self.name}，性别：{self.gender}，年龄：{self.age}，电话：{self.tel}"


print("==================================================")

# student1 = Student("demo1", 1, 22, 133)
# print(student1)
