# 体会一下range的用法
# 1是开始位置，10结束位置，1表示步长
print("==================================================")
for i in range(1, 10, 1):
    print("步长为1：", i)
# 在设置起始结束位置的情况下，1是包含的，10不包含
print("==================================================")
for i in range(1, 10, 2):
    print("步长为2：", i)
print("==================================================")
for i in range(10):
    print("不设置步长：", i)
# 不设置步长和起始位置，默认0-9