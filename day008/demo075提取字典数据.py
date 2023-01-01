dict1 = {"demo1": 100, "demo2": 166, "demo3": 150, "demo4": 200}
dict2 = {i: j for i, j in dict1.items() if j > 151}
print(dict2)  # {'demo2': 166, 'demo4': 200}
