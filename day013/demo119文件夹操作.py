import os

print("==================================================")
os.rename("demo120.txt", "demo120修改后.txt")  # 重命名文件
os.remove("demo120修改后.txt")  # 直接删除文件
