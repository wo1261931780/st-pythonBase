demo = "show me the money"
print(demo.isalpha())  # 判断是否全部为字母，空格也会返回false
demo2 = "show"
print(demo2.isalpha())  # 只要有一个非字母的字符存在，就是false
print("==================================================")
demo3 = "123demo"
print(demo3.isdigit())
print("==================================================")
demo4 = "123"
print(demo4.isdigit())  # 同理，必须全部数字
print("==================================================")
demo5 = "demo123"
print(demo5.isalnum())  # 判断是否是数字+字母组合
print("==================================================")
demo6 = ""
