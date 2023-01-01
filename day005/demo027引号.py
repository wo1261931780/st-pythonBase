# python中，字符串可以是1-3个引号

demo = 'demo1'
demo2 = "demo2"
demo3 = '''demo3'''
print(demo)
print(type(demo))
print(type(demo2))
print(type(demo3))
demo4 = '''123 1
111'''
print(demo4)  # 多行注释，类型不会发生变化
# 同时还允许内部换行
