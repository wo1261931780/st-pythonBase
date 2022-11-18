demo = "0123456"
print("全长：", demo)
print("切片：", demo[0:2:1])  # 12
# 表示从0开始，到2结束
# 切片的步长为1
# 步长指的是获取下一个字符的间隔
# 比如上面从0开始，步长为1，那么第二次获取就是1号，第三次获取就是2号
print("切片：", demo[0:2:2])  # 0
print("切片：", demo[0:3:2])  # 02
# 同理，这里从0开始，步长2，获取0号，第二次获取间隔2，获得2
# 实际上，这里的指针是在3号位，应该包括3，但是后面是开区间，3不在里面
# 所以只能拿到0和2

# 下一次获取，应该是拿到4
print("==================================================")
print("切片：", demo[:3])  # 012
# 这是省略写法，0号默认存在，步长默认为1
print("切片：", demo[3:])  # 3456
# 结束不写，默认从3号位置开始，到最后
print("切片：", demo[:])  # 0123456
# 这样写也是合理的
print("==================================================")
print("切片：", demo[::-1])  # 6543210
# 这里省略了开始和结束，步长设置负数
print("切片：", demo[::-2])  # 6420
# 只要步长是负数，就是倒序，步长的设置还是会生效的
