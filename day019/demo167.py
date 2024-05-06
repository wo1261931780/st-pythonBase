for i in range(1, 101):
	mark = int(input("输入" + str(i) + "个人的成绩"))
	if mark >= 90:
		print(str(i) + "号同学优秀")
		# grade = "优秀"
	elif mark >= 80:
		print(str(i) + "号同学良好")
	elif mark >= 60:
		print(str(i) + "号同学及格")
	else:
		print(str(i) + "号同学不及格")
# print(grade)
