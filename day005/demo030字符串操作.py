demo = "demo show me the money junw 123456 show"
# 在python中，一个单词就可以作为一个子字符串

print("junw结果为：", demo.find("junw"))  # 结果存在返回字符串的开始位置
print("55555结果为：", demo.find("55555"))  # -1，结果不存在返回-1
print("show结果为：", demo.find("show"))  # 5，空格也算一个字符
print("show结果为：", demo.find("show"))  # 5，如果有多个相同字符出现，那么保留最前面的这个
print("show结果为：", demo.find("show", 10, 20))  # 从10到20中间的字符串寻找
print("==================================================")

# print("show结果为：", demo.index("show", 10, 20))  # 使用index查询字符串，如果不存在就会直接报错
print("show结果为：", demo.index("show"))

print("==================================================")

print("count结果为：", demo.count("show", 10, 20))  # 0，不存在就是0
print("count结果为：", demo.count("show"))  # 计数2

print("==================================================")

print("show结果为：", demo.rindex("show"))  # 35 ，从右侧开始查找，但是索引还是正常顺序的

print("==================================================")
