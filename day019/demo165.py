import random

# 生成10位同学的成绩
scores = [random.randint(1, 100) for _ in range(10)]

print(f"10位同学的原始成绩为:\n{scores}")

# 排序，升序输出
sorted_scores = sorted(scores)
print(f"排序后，这10位同学成绩为:\n{sorted_scores}")

# 计算平均分，保留小数点后两位
average_score = round(sum(scores) / len(scores), 2)
print(f"平均分:{average_score}; 超过平均分人数:", end='')

# 超过平均分的人数
above_average_count = len([score for score in scores if score > average_score])
print(f"{above_average_count}人")

# 分数段统计
distribution = {
	'90-100': 0,
	'80-89': 0,
	'70-79': 0,
	'60-69': 0,
	'60以下': 0
}

for score in scores:
	if score >= 90:
		distribution['90-100'] += 1
	elif score >= 80:
		distribution['80-89'] += 1
	elif score >= 70:
		distribution['70-79'] += 1
	elif score >= 60:
		distribution['60-69'] += 1
	else:
		distribution['60以下'] += 1

print("每个分数段人数统计:")
for range in distribution:
	print(f"{range}: {distribution[range]}人")

# 选做：按各分数段人数降序排列
# 创建一个由分数段和对应人数组成的列表
distribution_sorted = sorted(distribution.items(), key=lambda item: item[1], reverse=True)

print("\n按各分数段人数降序排列:")
for range, count in distribution_sorted:
	print(f"{range}: {count}人")
