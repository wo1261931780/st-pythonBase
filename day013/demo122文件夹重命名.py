import os

print("==================================================")
# os.rename()  # 和之前的重命名是一样的，只不过这里是重命名文件夹
os_listdir = os.listdir()
print(type(os_listdir))  # <class 'list'>
# 返回的是一个list类型的结果
print(os_listdir)
for i in os_listdir:
    new_name = "new_name" + i
    os.rename(i, new_name)
    # 两个参数，原始的文件名和重命名之后的文件名
