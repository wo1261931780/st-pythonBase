i = 1
demo = 0
while i <= 100:
    if i % 2 == 0:
        demo += i
        print(demo)
    i += 1
# 实际有两种思路可以完成
# 一种是每次累加2，一种是单纯累加偶数
print(demo)
print("==============================")


def main():
    j = 0
    demo1 = 0
    while j <= 100:
        demo1 += j
        j += 2
        print(demo1)
    print("==============================")
    print(demo1)


if __name__ == '__main__':
    main()
