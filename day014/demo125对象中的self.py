class Demo:
    def demo_run(self):
        print(self)  # <__main__.Demo object at 0x0000027BFEAEBF40>
        print("demo类运行")


demo1 = Demo()
print(demo1)  # <__main__.Demo object at 0x0000027BFEAEBF40>
demo1.demo_run()
print("==================================================")
