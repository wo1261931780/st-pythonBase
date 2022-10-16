name = "demo"
age = 18
weight = 100

print("名字%s，年龄%s，体重%s" % (name, age, weight))
# 可以全部作为字符串输出
print(f"我的名字{name}，今年{age}岁")
# 效果一样，但是更加高效

# 这里注意一下转义符
# /这是斜杠，\这是反斜杠
print("demo1")
print("demo2")
print("demo1\ndemo2")  # 转义字符只会转化一个单词，中间如果添加空格，会不符合我们需要的排版
# 反斜杠\n，就是换行转义字符
print("demo1\tdemo2")  # 换行转义符，代表四个空格

# 如果是\t就表示制表符的缩进
