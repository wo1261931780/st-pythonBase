text_io = open("demo109.txt", "r+")
# text_io_read = text_io.read()  # 默认读取所有数据
# 换句话来说，指针在开头
# print(text_io_read)
# print("==================================================")
# text_io.seek(2, 0)  # 跳过两个字符，修改指针位置
# 第一个变量，表示偏移量
# 第二个变量，表示指针的起始位置
text_io.seek(0, 2)
print(text_io.read())
print("==================================================")
text_io.close()
