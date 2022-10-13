num001 = 1
num002 = 2.1
print(type(num001))  # <class 'int'>
print(type(num002))  # <class 'float'>
# 这里会自动区分数据类型
# print("我是数据类型：" + type(num001))
print("=====================================")
str001 = "12"
str002 = "字符串"
print(type(str001))  # <class 'str'>
print(type(str002))  # <class 'str'>
print("=====================================")
demo001 = True
# 这里需要注意：布尔类型的是区分大小写的
print(type(demo001))  # <class 'bool'>
print("=====================================")
demo002 = [1, 1, 2, 3]
print(demo002)  # 数组中的数据是可以重复的
print(type(demo002))  # <class 'list'>
print("=====================================")
demo003 = (6, 12, 5, 3, 3, 45)  # <class 'tuple'>
print(demo003)  # 元祖中的数据也可以重复
# 小括号表示的是元组类型
print(type(demo003))
print("=====================================")
demo004 = {1, 1, 2, 2, 2, 3}
print(demo004)  # {1, 2, 3}
print(type(demo004))  # set类型的就不允许出现重复的元素
print("=====================================")
demo005 = {"a1": 1, "demo": "002"}
print(demo005)  # 所见即所得，{'a1': 1, 'demo': '002'}
# 说实在的，这种键值对的形式，我觉得就是json
print(type(demo005))  # 字典类型，<class 'dict'>
1
