import os

# print("==================================================")
os.mkdir("demo122folder")  # 创建文件夹

print("==================================================")
os.rmdir("demo122folder")  # 删除文件夹

print("==================================================")
print(os.getcwd())  # C:\Users\64234\Documents\GitHub\st-python.github.io\day013
# 返回当前文件的所在路径
# 这里返回的，是当前py文件的所在位置
print("==================================================")
# os.mkdir("demo122folder")  # 对于已经存在的文件夹，继续创建会导致报错
# os.chdir("demo122folder") # 切换当前路径
# os.mkdir("demo122folder2")
print(os.listdir())
# ['demo108文件操作.py', 'demo109.txt', 'demo110访问模式.py', 'demo111读取函数.py', 'demo112readlines函数.py', 'demo113readline函数.py', 'demo114代码测试.py', 'demo115seek函数.py', 'demo116文件备份.py', 'demo117数据写入.py', 'demo118.txt', 'demo119文件夹操作.py', 'demo120修改后.txt', 'demo121创建和删除.py']
# 一次性获取到了当前路径下的所有文件
