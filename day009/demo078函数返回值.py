def bug_cigarette(num):
    if num == 10:
        return "cigarette"
        # 这里和java一样，不会执行return后面的语句
    else:
        return "get out"


cigarette = bug_cigarette(10)
print(cigarette)
