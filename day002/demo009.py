num1 = 1
num2 = "111"
print(type(num1))
print(type(int(num2)))  # 强制转化为<class 'int'>
str1 = "demo"
# print(type(int(str1)))  # 字符串直接转化，会出现异常
# invalid literal for int() with base 10: 'demo'
# 下面是整数转化为字符串
print(type(str(num1)))
demoCollection = [1, 12, 2, 313, "123"]
print(type(tuple(demoCollection)))
demoList = (1, 2, 31, 24)
print(type(list(demoList)))  # <class 'list'>
print("==================================================")

demoStr1 = "1"
demoStr2 = "1.11"
demoStr3 = "demo"
demoStr4 = "(1,1,1,2)"
demoStr5 = "[1,1,1,2]"
# 下面使用eval可以自动识别字符串中的数据类型
# 然后将其转化为具体的数据类型
print(type(eval(demoStr1)))  # <class 'int'>
print(type(eval(demoStr2)))  # <class 'float'>
# print(type(eval(demoStr3))) #直接转化本身就是字符串的类型，会导致报错
print(type(eval(demoStr4)))  # <class 'tuple'>
print(type(eval(demoStr5)))  # <class 'list'>
