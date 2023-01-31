# 将一个字符串提取出来

demo = "0x123456ff"
print(len(demo))  # 10
print(demo)
print(demo[2:10])
demo1 = demo[2:10]
print(type(demo1))
# 然后将提取出来的字符串，转化为16进制的数据类型

i = int(demo1, 16)
print(i)
print(type(i))
