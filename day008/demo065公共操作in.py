str1 = 'demo1'
t3 = (1, 2)
dict5 = {"dict5": "555"}
list7 = [11, 22]
print("==================================================")
print("demo" in str1)  # True
# 对于字符串来说，只要有一部分存在，那就是全部返回true
# 我们可以这么理解：
# 字符串add到list中，是一个一个字符独立添加进去的
# 换句话来说，字符串中的每个单字，都是一个独立的对象
# 所以，就算字符串中只有一部分数据存在，也会返回true
print("==================================================")
print(1 in t3)  # True
print("1" in t3)  # False
print("==================================================")
print("dict5" in dict5)  # True
print("555" in dict5)  # False
# 不能直接根据value来测试是否存在于字典中
# 因为value可能相同，但是key一定不同，所以value不能作为判断依据
print("dict" in dict5)  # False
# 同样的，每个key都是唯一的，所以需要完整的判断
print("dict" in dict5.keys())  # False
# 是否存在于字典的key数组中
# print("==================================================")
print("55" in dict5.values())  # False
print("555" in dict5.values())  # True
# 但是要判断是否存在于字典中，还是可以使用这个方法
print("==================================================")
print(22 in list7)  # True
print("22" in list7)  # False
# 这里，list会判断数据类型是数据还是字符串
# 如果数据类型都不一样，就不可能是别的了
