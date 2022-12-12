import os

print("==================================================")

os_listdir = os.listdir()
print(os_listdir)
for i in os_listdir:
    rm_name = len("new_name")
    new_name = i[rm_name:]
    # new_name = "new_name" + i # 批量新增前缀
    os.rename(i, new_name)
