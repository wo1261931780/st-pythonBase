demo_list = ["the", "money"]

demo_list[0] = "show"
print(demo_list)
print("==================================================")
demo_list.reverse()
print(demo_list)  # 逆序排列
print("==================================================")
demo_list2 = [11, 2, 13, 4, 5]
demo_list2.sort()
print(demo_list2)  # [2, 4, 5, 11, 13]，默认升序排列
print("==================================================")
demo_list2.sort(reverse=True)  # [13, 11, 5, 4, 2]
# reverse控制是否降序排列
print(demo_list2)
