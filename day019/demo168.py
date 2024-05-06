from math import lcm

demo1 = 1
chushu1 = 15
chushu2 = 4
if chushu1 < chushu2:
	chushu1, chushu2 = chushu2, chushu1

print("较大的数是：", chushu1, "较小的数是：", chushu2)

while demo1 <= chushu1:
	print("------------------")
	print("当前demo1是：", demo1)
	yushu = chushu1 % chushu2
	print("余数是：", yushu)
	if yushu == 0:
		print("整除：", chushu2)
		break
	else:
		demo1 += 1

print("结果：", demo1)
