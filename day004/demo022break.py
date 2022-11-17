demo1 = 0
demo2 = 0

while demo1 <= 5:
    demo1 += 1
    if demo1 == 3:
        continue
    demo2 += 1
    print(demo2)
print(demo2)


def main():
    demo11 = 0
    demo22 = 0
    print("==========================")
    while demo11 <= 5:
        demo11 += 1
        if demo11 == 3:
            break
        demo22 += 1
        print(demo22)
    print(demo22)


if __name__ == '__main__':
    main()
