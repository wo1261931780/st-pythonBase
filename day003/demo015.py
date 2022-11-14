print("请输入年龄：")
# age = input()
# 不能直接进行比较，因为input接受到的默认是字符串类型
age = int(input())

if age > 18:
    print("成年")
else:
    print("未成年")
