# text_io = open("demo146.txt", "r")
# 报错信息：
# FileNotFoundError: [Errno 2] No such file or directory: 'demo146.txt'
# print(text_io)
print("==================================================")
try:
    text_io = open("demo146.txt", "r")
except:
    print("我有异常，这里是异常后的代码")
    text_io = open("demo146.txt", "w")
    print(text_io)
print("==================================================")
