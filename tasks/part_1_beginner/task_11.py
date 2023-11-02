num: str = input()
is_num: bool = True
digits: str = "0123456789"
symbols: str = "+-. "
dots_count: int = 0
for item in num:
    if (item not in digits) and (item not in symbols):
        is_num = False
        break
    elif item == ".":
        dots_count += 1
    if dots_count > 1:
        is_num = False
        break
print(is_num)
