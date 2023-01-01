def demo_run(name1, age1, gender1):
    print(f"姓名是：{name1}，年龄：{age1}，性别：{gender1}")


print("==================================================")
demo_run(11, 22, 33)
# demo_run(11, 22) # 缺少一个参数会直接报错
demo_run([11, 22, 33], (1, 1, 2), "demo")  # python不是强类型的
# 只要数量正常，不会纠结具体的参数类型
print("==================================================")

demo_run(name1="demo", gender1=0, age1=22)
# 姓名是：demo，年龄：22，性别：0
# demo_run(gender1=0, age1=22, "demo") # 参数顺序异常，会导致报错
demo_run("demo", gender1=0, age1=22)
