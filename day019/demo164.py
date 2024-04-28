def is_leap_year(year):
	"""判断指定的年份是否为闰年"""
	if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
		return True
	else:
		return False


# 用户输入年份
year = int(input("请输入一个年份来判断是否为闰年: "))

# 判断是否为闰年并输出结果
if is_leap_year(year):
	print(f"{year}是闰年")
else:
	print(f"{year}不是闰年")
