demo_list = ["the", "money"]

print("==================================================")
demo_list.insert(1, "demo")  # 在指定索引开始添加
# 比如1号原来元素是demo1，插入demo2，
# 那么1号的元素目前就是demo2，原来的demo1变成2号元素
print(demo_list)  # ['the', 'demo', 'money']
print("==================================================")
