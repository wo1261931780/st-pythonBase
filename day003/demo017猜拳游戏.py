import random

demo1 = 0
# 剪刀0，石头1，布2
while demo1 != -1:
    demo1 = int(input("请输入玩家出拳："))
    computer_demo2 = random.randint(0, 2)  # 这里的随机数包含了开始和结尾数字，
    print("电脑出拳：", computer_demo2)
    # 包含了0和2
    if computer_demo2 == demo1 and demo1 != -1:
        print("平局")
    elif computer_demo2 - demo1 == 1:
        print("电脑获胜")
    else:
        print("玩家获胜")

print("game over")
