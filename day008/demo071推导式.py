list1 = []
i = 0
while i < 5:
    list1.append(i)
    i += 1
print(list1)
print("==================================================")
list2 = []
for i in range(10):
    list2.append(i)
print(list2)
print("==================================================")
list3 = [i for i in range(5)]  # 这就是推导式
# 用来创建有规律的代码，降低代码量
print(list3)
