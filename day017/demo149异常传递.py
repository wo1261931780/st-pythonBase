print("demo")
try:
    text_io = open("demo150.txt")
    try:
        while True:
            text_io_readline = text_io.readline()
            if len(text_io_readline) == 0:
                break
            else:
                print(text_io_readline)
    except Exception as result1:
        print(f"出现{result1}==========》程序终止")
except Exception as result:
    print(result)
# finally:
#     text_io.close()
# 这里说明一下异常的传递
# 从外层传递到内层，一层层抛出异常
