dict1 = {"demo1": "111", "demo2": "222", "demo3": "333"}

print(dict1.keys())  # dict_keys(['demo1', 'demo2', 'demo3'])
# 相当于打印所有的key
# 可迭代的对象——可以通过循环来遍历
print("==================================================")
print(dict1.values())  # dict_values(['111', '222', '333'])
# 返回所有的值
print("==================================================")
print(dict1.items())
# dict_items([('demo1', '111'), ('demo2', '222'), ('demo3', '333')])
# 类似于java中的键值对同时打印出来
print("==================================================")
keys = dict1.keys()
print(type(keys))  # 得到的数据类型是<class 'dict_keys'>
print("==================================================")
print(type(dict1.values()))  # <class 'dict_values'>
print("==================================================")
print(type(dict1.items()))  # <class 'dict_items'>
items = dict1.items()
for i in items:
    print(i)  # ('demo1', '111')
    print(type(i))  # <class 'tuple'>

print("==================================================")
