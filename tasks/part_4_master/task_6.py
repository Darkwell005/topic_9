line: str = input()
flag: bool = True
d: str = ""
for item in line:
    if item not in d:
        d += item
    else:
        flag = False
print(flag)
