num1 = 1
num2 = 2
if num2 > num1:
    print("num2较大：", num2)
else:
    print("num1较大：", num1)
print("==================================================")

if num1 and num2 > 0:
    print("大于0")
else:
    print("小于0")
print("==================================================")
num3 = 3
print(num1 > num2 and num2 < num3)
# False
# 这里的逻辑运算和java一样，只不过使用的是英文表达，不是符号
print("==================================================")

print(num1 > num2 or num2 < num3)
print("==================================================")
print(not num1 > num2) #True
