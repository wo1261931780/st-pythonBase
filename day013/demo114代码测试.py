# text_io = open("demo109.txt", "r+")
# text_io_read = text_io.read()
# print(text_io_read)
# text_io.close()

# print("==================================================")
# text_io2 = open("demo109.txt", "w+")
# 如果这里只完成了读取，没有写入，就会直接报错
# text_io2__read = text_io2.read()
# print(text_io2__read)
# text_io2.close()
# print("==================================================")

text_io3 = open("demo109.txt", "a+")  # 文件指针在结尾
# 默认是读取不到数据的
text_io3__read = text_io3.read()
print(text_io3__read)
text_io3.close()
