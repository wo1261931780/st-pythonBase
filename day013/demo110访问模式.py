text_io = open("demo109.txt", "r")  # 如果不存在对应的文件，io流会直接报错
# text_io.write("aaa")  # io.UnsupportedOperation: not writable
# 因为是只读模式，所以写入会报错
text_io.close()
print("==================================================")

text_io2 = open("demo109.txt", "w")  # 在写入模式下面，不存在对应的文件会直接创建一个
text_io2.write("junw")
text_io2.close()
print("==================================================")

text_io3 = open("demo109.txt", "a")  # 追加模式也会新建一个不存在的文件
# 和写入模式不同，追加模式不会覆盖之前的内容
text_io3.write("111")
text_io3.close()
print("==================================================")
text_io4 = open("demo109.txt")  # 访问模式可以省略访问类型
text_io4.close()
