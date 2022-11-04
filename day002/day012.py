num1 = 1
num1 += 2
print(num1)  # 结果为3，a=a+2
num2 = 10
num2 *= 1 + 2
print(num2)  # 结果为30，num2=num2*(1+2)

# 这里的逻辑，都是先计算右边的表达式结果，然后再执行复合运算


num3 = 10
num3 += 1 + 2
print(num3)  # 最后结果为13，a=a+(1+2)
