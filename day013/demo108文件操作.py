text_io = open("demo109.txt", "w")
# w表示写入操作
print(text_io)  # <_io.TextIOWrapper name='demo109.txt' mode='w' encoding='cp936'>
text_io.write("junw")  # 直接写入的时候，会删除原来的内容，然后将需要的内容写入
text_io.close()
