def demo_run(num):
    if num == 1:
        return 1
    return num + demo_run(num - 1)


print("==================================================")

print(demo_run(10))
