dict1 = {"demo1": "111", "demo2": "222", "demo3": "333"}

print(dict1["demo1"])
print("==================================================")
print(dict1.get("demo1"))
print(dict1.get("show"))  # 不存在的元素，无法返回，所以得到None
print(dict1.get("show", "null"))  # 在这里也可以自定义返回的结果，可以设置返回第二个参数：null
