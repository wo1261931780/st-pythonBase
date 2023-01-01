class Exception_self(Exception):
    def __init__(self, length, demain):
        self.length = length
        self.demain = demain

    def __str__(self):
        return f"你输入的密码长度{self.length}，不能少于{self.demain}个字符"


def input_paw():
    try:
        input_str1 = input("请输入密码：")
        min_len = 3
        if len(input_str1) < min_len:
            raise Exception_self(len(input_str1), min_len)
        # raise就是手动抛出异常
    except Exception as result:
        print(result)
    else:
        print("您的密码已经输入完成")


print("==================================================")
input_paw()
