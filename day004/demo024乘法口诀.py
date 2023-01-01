demo = 0
while demo <= 8:
    demo += 1
    demo1 = 0
    while demo1 < demo:
        demo1 += 1
        # print(demo, "*", demo1, "=", demo * demo1, end="\t")
        # 用一些好的代码
        print(f"{demo}*{demo1}={demo * demo1}", end="\t")
    print()
print("===========结束============")
