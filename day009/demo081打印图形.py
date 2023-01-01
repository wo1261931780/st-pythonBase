def print_line():
    print("*" * 20)
    # print("end")


print_line()
print("==================================================")


def print_lines(nums):
    i = 0
    while i < nums:
        print_line()
        i += 1


print_lines(5)
