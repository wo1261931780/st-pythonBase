demo = 0
while demo < 5:
    demo += 1
    print(demo)
    if demo == 3:
        print("提前终止")
        break
else:
    print('正常结束')
print("============结束============")
# while……else里面有个问题
# 如果while循环中直接进行break
# 那么else中的代码是不会出现的
# 但是循环体外面的代码不受影响
