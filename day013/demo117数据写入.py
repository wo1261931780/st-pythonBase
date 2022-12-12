input_str1 = input("请写入文件名")
print(input_str1)
print("==================================================")
input_str__rfind = input_str1.rfind(".")
print(input_str__rfind)
print("==================================================")

binary_ior = open("demo109.txt", "rb")
print(binary_ior)  # <_io.BufferedReader name='demo109.txt'>
# 单纯读取
binary_iow = open("demo118[拷贝结果].txt", "wb")
# 单纯写入，因为写入会自动创建文件，所以不需要保证文件存在
print(binary_iow)
print("==================================================")
if input_str__rfind > 0:  # 如果是有效文件才会进行读写操作
    while True:
        binary_ior_read = binary_ior.read(1024)
        print(binary_ior_read)
        if len(binary_ior_read) == 0:
            break
        binary_iow.write(binary_ior_read)

binary_ior.close()
binary_iow.close()
