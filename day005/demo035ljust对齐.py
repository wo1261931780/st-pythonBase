demo = "show me the money"
demo_t_ljust = demo.ljust(30)  # show me the money
print(demo_t_ljust)  # 默认用空格填充需要的30位长度
print("==================================================")
demo_t_ljust2 = demo.ljust(30, ".")  # 必须使用数字，然后用点号补充即可
print(demo_t_ljust2)  # show me the money.............
print("==================================================")
demo_rjust = demo.rjust(30, ".")
print(demo_rjust)
print("==================================================")
demo_center = demo.center(30, ".")
print(demo_center)
