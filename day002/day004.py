# 格式化输出

# 字符串，string，格式化就是%s
# 有符号的十进制整数
# 有无符号，区别就在于，数字之前是否能添加正负符号
# 用来表示正负整数
print("==================================================")

# 如果十进制的整数没有符号，那么默认这是一个正整数
age = 18
print(age)
# print("今年的年龄" + age + "岁")  # python有点类似于html，
# 如果没有报错，会一直执行下去，
# 但是出现了报错，就会停在报错的那一行代码
print("今年的年龄是%d岁" % age)
print("==================================================")

name = 'junw'
print("我的名字%s" % name)
print("==================================================")

weight = 100.00
print("体重是%f" % weight)  # 体重是100.000000
# 就算没有足够的小数位数，最后也会补齐
print("体重是%.2f" % weight)  # 体重是100.00
# 这里就会只保留两位小数
print("==================================================")
st_id1 = 123
st_id2 = 1
st_id3 = 1234
print("测试转换数字为字符串%d" % st_id1)  # 这里不能当做字符串处理
# 需要当成数字进行格式化操作
print('测试转换数字为字符串%03d' % st_id1)  # 格式化，保留三个数字
print("测试转换数字为字符串%03d" % st_id2)  # 不足三个数字的，使用0补全
print("测试转换数字为字符串%03d" % st_id3)  # 超过三个数字的，就保留所有
print("==================================================")
print("我的名字是%s，今年%d岁了" % (name, age))
# 面对多个数字的展示，这里就需要使用统一格式化的方法来操作
print("我的名字是%s，明年%d岁了" % (name, age + 1))

print("==================================================")
print("我的名字%s,今年%d岁，体重%.2f公斤，学号%03d" % (name, age, weight, st_id3))
