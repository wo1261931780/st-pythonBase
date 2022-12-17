# 我们在python中导入的模块，实际上就是外部库中一个个的py文件
import math
from math import sqrt

# 换句话来说，这样一个个的py文件，实际上就是内部定义了一个个的python函数
print("==================================================")

math_sqrt = math.sqrt(9)
print(math_sqrt)  # 3.0
# 和除法一样，会得到一个浮点数据
print(sqrt(16))
# from math import sqrt
# 通过这种方式导入，就可以省略math前缀
