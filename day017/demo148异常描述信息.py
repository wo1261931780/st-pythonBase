try:
    print(demo)
except Exception as result:
    print(result)
else:
    print("我是没有异常的时候执行的代码")
finally:
    print("我是一定会执行的代码")

print("==================================================")

# 这里和java一样，直接捕获所有的异常描述信息即可
# 但是这里有个问题，没有说明具体的异常类型
