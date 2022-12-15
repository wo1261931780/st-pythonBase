class Demo:
    name = 11  # 类属性
    # 类属性更加节约内存空间


demo1 = Demo()  # 这个是实例属性，属于新建出来的对象
print(f"我是demo1中的name属性：{demo1.name}")
print("==================================================")

Demo.name = 22  # 通过类名，修改类属性，会全局生效
demo2 = Demo()
print(f"我是demo1中的name属性：{demo1.name}")
print(f"我是demo2中的name属性：{demo2.name}")
print("==================================================")

demo1.name = 33
print(f"我是demo1中的name属性：{demo1.name}")
print(f"我是demo2中的name属性：{demo2.name}")
