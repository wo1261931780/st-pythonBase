print("==================================================")
text_io = open("demo109.txt")
print(text_io.readline())  # junw111
# 一行一行地读取，不会读取到换行符
print(text_io.readline())  # 11111
text_io.close()
